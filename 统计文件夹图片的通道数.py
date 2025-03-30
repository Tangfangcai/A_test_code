import os
import rasterio
from collections import defaultdict

def count_tif_channels(folder_path):
    channel_counts = defaultdict(int)  # 统计不同通道数的数量
    total_files = 0

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(".tif"):  # 仅处理 .tif 文件
            file_path = os.path.join(folder_path, file_name)
            try:
                with rasterio.open(file_path) as src:
                    num_channels = src.count  # 获取通道数
                    channel_counts[num_channels] += 1  # 统计该通道数的文件数量
                    total_files += 1
            except Exception as e:
                print(f"⚠️ 处理 {file_name} 时出错: {e}")

    return channel_counts, total_files

# 指定文件夹路径
folder_path = "./新建文件夹"  # 替换成你的文件夹路径
channel_counts, total_files = count_tif_channels(folder_path)

# 打印统计结果
print(f"📂 统计结果（文件夹: {folder_path}）：")
print(f"📄 总文件数: {total_files}")
for channels, count in sorted(channel_counts.items()):
    print(f"📊 {channels} 通道文件数: {count}")
