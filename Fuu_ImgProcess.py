import os
import filecmp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def remove_duplicate_files(folder_path):
    folder = Path(folder_path)
    if not folder.is_dir():
        print("Invalid folder path.")
        return

    file_list = list(folder.glob('*'))  # 获取文件夹中的所有文件

    for i in range(len(file_list)):
        file1 = file_list[i]
        if not file1.exists():
            continue

        for j in range(i + 1, len(file_list)):
            file2 = file_list[j]
            if not file2.exists():
                continue

            if filecmp.cmp(file1, file2, shallow=False):  # 如果文件内容相同
                print(f"Duplicate files found: {file1} and {file2}")
                file2.unlink()  # 删除其中一个文件
                print(f"Removed {file2}")





def split_image(image_path, output_folder):
    # 将图片十字4分的函数，分割好的图片输出到output
    # 需要注意的是，在做分割前需要给图片重命名
    img = Image.open(image_path)
    img_name = os.path.splitext(os.path.basename(image_path))[0]
    width, height = img.size
    half_width = width // 2
    half_height = height // 2
    img1 = img.crop((0, 0, half_width, half_height))
    img2 = img.crop((half_width, 0, width, half_height))
    img3 = img.crop((0, half_height, half_width, height))
    img4 = img.crop((half_width, half_height, width, height))
    img1.save(os.path.join(output_folder, f"{img_name}_1.png"))
    img2.save(os.path.join(output_folder, f"{img_name}_2.png"))
    img3.save(os.path.join(output_folder, f"{img_name}_3.png"))
    img4.save(os.path.join(output_folder, f"{img_name}_4.png"))


def process_splitimages(input_folder, output_folder):
    # 将Input中的文件分割并将结果输出到output
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, file)
            split_image(image_path, output_folder)


def add_watermark(input_image_path, output_image_path, watermark_text):
    # 打开原始图片
    base_image = Image.open(input_image_path).convert("RGBA")
    # 创建一个与原图大小相同的透明图片
    txt = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
    # 获取字体
    #font = ImageFont.truetype("arial.ttf", int(base_image.size[1] * 0.1))
    font = ImageFont.truetype("./VonwaonBitmap.ttf", int(base_image.size[1] * 0.1))
    # 初始化画布
    d = ImageDraw.Draw(txt)
    # 计算文字位置
    text_size = d.textsize(watermark_text, font)
    text_position = (int((base_image.size[0] - text_size[0]) / 2), int((base_image.size[1] - text_size[1]) / 2))
    # 将水印文字绘制到透明图片上
    d.text(text_position, watermark_text, font=font, fill=(255, 255, 255, 128))
    # 将两张图片合并
    watermarked = Image.alpha_composite(base_image, txt)
    # 保存添加水印后的图片
    watermarked.convert("RGB").save(output_image_path)

def process_watermarkImgs(watermark_text ,input_folder ,output_folder ):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for image_name in os.listdir(input_folder):
        input_image_path = os.path.join(input_folder, image_name)
        output_image_path = os.path.join(output_folder, image_name)
        add_watermark(input_image_path, output_image_path, watermark_text)

if __name__ == "__main__":
    OriginImgs = "./OriginImgs"
    SplitedImgs = "./SplitedImgs"
    WateredImgs = "./WateredImgs"
    WaterMarkText = "挖煤医生，向你问好！"

    print("批量图片处理工具 V1.0 by 挖煤医生@bilibili")
    print("请确保你的python环境已安装以下类库: pillow, rembg")
    print("默认原图文件夹（四格图）:OriginImgs \n 默认分割文件夹（单图）:SplitedImgs \n 默认水印文件夹:WateredImgs")
    print("默认水印文本：挖煤医生，向你问好")
    remove_duplicate_files(OriginImgs)
    process_splitimages(OriginImgs, SplitedImgs)
    process_watermarkImgs(WaterMarkText, SplitedImgs, WateredImgs )
    pass