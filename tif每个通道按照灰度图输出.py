import rasterio
import numpy as np

# 读取 TIFF 文件
tif_path = "./tif/000165.tif"  # 替换为你的 TIFF 文件路径
with rasterio.open(tif_path) as src:
    image = src.read()  # 读取所有通道
    profile = src.profile  # 获取元数据（如宽度、高度、投影等）

# 将每个通道转换为 8 位灰度图
for i in range(image.shape[0]):  # 遍历每个通道
    channel = image[i]  # 获取当前通道

    # 将数据范围缩放到 [0, 255]
    channel_min = np.min(channel)
    channel_max = np.max(channel)
    # channel_normalized = (channel - channel_min) / (channel_max - channel_min) * 255
    channel_normalized = channel
    
    channel_8bit = channel_normalized.astype(np.uint8)  # 转换为 uint8

    # 更新元数据中的数据类型
    profile.update(dtype=np.uint8, count=1)  # 设置为单通道，8 位

    # 保存当前通道为 8 位灰度 TIFF 文件
    output_path = f"./tif/000165_channel_{i+1}_8bit.png"  # 替换为输出文件路径
    with rasterio.open(output_path, "w", **profile) as dst:  # 确保没有不可见字符
        dst.write(channel_8bit, 1)  # 写入数据

    print(f"通道 {i+1} 已保存为 8 位灰度图: {output_path}")