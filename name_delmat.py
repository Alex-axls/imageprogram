# 参考CSDN 把图片名字.mat.png里面的.mat去掉，使其和标签文件txt的名字匹配 
import os
base_path = 'E:/pythonProject/ultralytics-main/PPI/images'
label_path = 'E:/pythonProject/ultralytics-main/PPI/labels'
def rename_files(src_dir):
    for file_name in os.listdir(src_dir):
        if file_name.endswith('.mat.png'):
            new_name = file_name.replace('.mat.png', '.png')
            os.rename(os.path.join(src_dir, file_name), os.path.join(src_dir, new_name))
            print(f"Renamed {file_name} to {new_name}")

# 重命名train目录下的图片
rename_files(os.path.join(base_path, 'train'))
# 重命名val目录下的图片
rename_files(os.path.join(base_path, 'val'))
# 重命名test目录下的图片
rename_files(os.path.join(base_path, 'test'))
def check_files(src_dir):
    for file_name in os.listdir(src_dir):
        if file_name.endswith('.png'):
            label_file_name = file_name.replace('.png', '.txt')
            if not os.path.exists(os.path.join(label_path, label_file_name)):
                print(f"Label file {label_file_name} not found for image {file_name}")

# 检查train目录下的图片和标签
check_files(os.path.join(base_path, 'train'))
# 检查val目录下的图片和标签
check_files(os.path.join(base_path, 'val'))
# 检查test目录下的图片和标签
check_files(os.path.join(base_path, 'test'))