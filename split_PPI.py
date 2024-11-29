#https://blog.csdn.net/m0_63774211/article/details/135271794 划分training val test
import os
import shutil
import random

# 定义源路径和目标路径
base_path = 'E:/pythonProject/ultralytics-main/PPI/images'
label_path = 'E:/pythonProject/ultralytics-main/PPI/label_txt'
output_dir = 'E:/pythonProject/ultralytics-main/PPI/split'

# 创建输出目录
os.makedirs(output_dir, exist_ok=True)
os.makedirs(os.path.join(output_dir, 'train'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'val'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'test'), exist_ok=True)

# 获取所有图片和标签文件
image_files = [f for f in os.listdir(base_path) if f.endswith('.jpg') or f.endswith('.png')]
label_files = [f for f in os.listdir(label_path) if f.endswith('.txt')]

# 确保图片和标签文件数量一致
assert len(image_files) == len(label_files), "图片和标签文件数量不一致"

# 打乱文件顺序
random.shuffle(image_files)

# 计算分割点
total_files = len(image_files)
train_split = int(0.8 * total_files)
val_split = int(0.9 * total_files)

train_images = image_files[:train_split]
val_images = image_files[train_split:val_split]
test_images = image_files[val_split:]

# 分割文件到不同的文件夹
def move_files(file_list, src_dir, dst_dir):
    for file_name in file_list:
        # 移动图片
        shutil.move(os.path.join(src_dir, file_name), os.path.join(dst_dir, file_name))
        # 移动对应的标签文件
        label_file_name = file_name.split('.')[0] + '.txt'
        shutil.move(os.path.join(label_path, label_file_name), os.path.join(dst_dir, label_file_name))

# 移动train文件
move_files(train_images, base_path, os.path.join(output_dir, 'train'))
# 移动val文件
move_files(val_images, base_path, os.path.join(output_dir, 'val'))
# 移动test文件
move_files(test_images, base_path, os.path.join(output_dir, 'test'))

print("文件分割完成！")

print(f"Train images: {len(os.listdir(os.path.join(output_dir, 'train')))}")
print(f"Val images: {len(os.listdir(os.path.join(output_dir, 'val')))}")
print(f"Test images: {len(os.listdir(os.path.join(output_dir, 'test')))}")