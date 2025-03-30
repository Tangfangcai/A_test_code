from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 打开 PNG 文件
image_path = "./tif/000165.png"  # 替换为你的 PNG 文件路径
image = Image.open(image_path)

# 将图像转换为 NumPy 数组
image_array = np.array(image)

# 检查图像是否为 RGB 格式
if image_array.ndim != 3 or image_array.shape[2] != 3:
    raise ValueError("图像必须是 RGB 格式（3 个通道）")

# 分离 RGB 通道
r_channel = image_array[:, :, 0]  # 红色通道
g_channel = image_array[:, :, 1]  # 绿色通道
b_channel = image_array[:, :, 2]  # 蓝色通道

# 显示原始图像和 RGB 通道
plt.figure(figsize=(12, 4))

# 显示原始图像
plt.subplot(1, 4, 1)
plt.title("Original Image")
plt.imshow(image_array)
plt.axis("off")

# 显示红色通道
plt.subplot(1, 4, 2)
plt.title("Red Channel")
plt.imshow(r_channel, cmap="gray")
plt.axis("off")

# 显示绿色通道
plt.subplot(1, 4, 3)
plt.title("Green Channel")
plt.imshow(g_channel, cmap="gray")
plt.axis("off")

# 显示蓝色通道
plt.subplot(1, 4, 4)
plt.title("Blue Channel")
plt.imshow(b_channel, cmap="gray")
plt.axis("off")

# 调整布局并显示
plt.tight_layout()
plt.show()


