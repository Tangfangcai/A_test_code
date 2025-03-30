import rasterio
import numpy as np
import matplotlib.pyplot as plt

# 读取 TIFF 文件
tif_path = "./tif/000165.tif"  # 替换为你的 TIF 文件路径
with rasterio.open(tif_path) as src:
    image = src.read()  # 读取所有通道
    num_channels = image.shape[0]  # 获取通道数
    dtype = image.dtype  # 获取数据类型

print(f"图像形状: {image.shape}（通道数, 高度, 宽度）")



print(f"数据类型: {dtype}")

# 根据数据类型推断位深
if dtype == np.uint8:
    bit_depth = 8
elif dtype == np.uint16:
    bit_depth = 16
elif dtype == np.float32:
    bit_depth = 32
elif dtype == np.float64:
    bit_depth = 64
else:
    bit_depth = "未知"

print(f"图像位深: {bit_depth} 位")




# 创建一个大小为 10x6 英寸的图形窗口
plt.figure(figsize=(10, 6))

for i in range(num_channels):
    plt.subplot(1, num_channels, i + 1)
    plt.title(f"Channel {i + 1}")
    im = plt.imshow(image[i], cmap="gray")
    plt.colorbar(im, orientation="vertical", pad=0.1)  # 添加颜色条
    plt.axis("off")  # 关闭坐标轴

plt.tight_layout()  # 自动调整子图布局
plt.show()

# # 保存图像
# output_path = "./output/tif_channels.png"
# plt.savefig(output_path, bbox_inches="tight", dpi=300)
# print(f"图像已保存到: {output_path}")





