from PIL import Image

def convert_png_to_ico(png_path, ico_path, sizes=None):
    if sizes is None:
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
    try:
        image = Image.open(png_path)
        image.save(ico_path, format='ICO', sizes=sizes)
        print(f"成功将 {png_path} 转换为 {ico_path}")
    except Exception as e:
        print(f"转换时出现错误: {e}")

if __name__ == "__main__":
    png_file = 'icon.png'  # 替换为你的 PNG 文件路径
    ico_file = 'icon.ico'  # 替换为你想要保存的 ICO 文件路径
    convert_png_to_ico(png_file, ico_file)
    