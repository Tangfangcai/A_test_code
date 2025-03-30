import rasterio
import numpy as np
import cv2
import pywt
import matplotlib.pyplot as plt

# 读取 SAR 图像
def read_sar_image(file_path):
    with rasterio.open(file_path) as src:
        sar_img = src.read()  # 形状：(C, H, W)
    return sar_img

# 高斯滤波（对每个通道应用）
def apply_gaussian_filter(img, kernel_size=5, sigma=1):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)

# 小波变换（对每个通道应用）
def wavelet_transform(img, wavelet='haar'):
    coeffs2 = pywt.dwt2(img, wavelet)
    LL, (LH, HL, HH) = coeffs2
    return LL  # 只返回低频部分（去噪）

# 处理 SAR 图像（适配不同通道数）
def process_sar_image(file_path):
    sar_img = read_sar_image(file_path)
    num_channels, H, W = sar_img.shape  # 读取通道数
    
    filtered_images = []
    wavelet_images = []

    for i in range(num_channels):  # 逐通道处理
        filtered = apply_gaussian_filter(sar_img[i])
        wavelet_img = wavelet_transform(filtered)
        filtered_images.append(filtered)
        wavelet_images.append(wavelet_img)

    return np.array(filtered_images), np.array(wavelet_images)

# 显示原图、高斯滤波、小波变换的效果
def show_results(file_path):
    sar_img = read_sar_image(file_path)
    filtered_imgs, wavelet_imgs = process_sar_image(file_path)

    num_channels = sar_img.shape[0]

    plt.figure(figsize=(10, 4 * num_channels))
    for i in range(num_channels):
        plt.subplot(num_channels, 3, i * 3 + 1)
        plt.title(f"Original (Ch {i+1})")
        plt.imshow(sar_img[i], cmap="gray")

        plt.subplot(num_channels, 3, i * 3 + 2)
        plt.title(f"Gaussian Filtered (Ch {i+1})")
        plt.imshow(filtered_imgs[i], cmap="gray")

        plt.subplot(num_channels, 3, i * 3 + 3)
        plt.title(f"Wavelet Transform (Ch {i+1})")
        plt.imshow(wavelet_imgs[i], cmap="gray")

    plt.show()

# 测试代码
file_path = "tif\Cargo_x48978_y3775.tif"  # 替换成你的文件路径
show_results(file_path)
