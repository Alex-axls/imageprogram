#把雷达学报PPI的bmp转成pnghttps://mp.weixin.qq.com/s/iOppHql3zDXiGFY_Alh9oA,
#裁剪重点区域https://mp.weixin.qq.com/s/pPZoYya1t-KkGUymWLo8Ww
import os
label_dir = 'E:/pythonProject/ultralytics-main/PPI/labels'
image_width = 520
image_height = 520
def modify_labels(src_dir):
    for file_name in os.listdir(src_dir):
        if file_name.endswith('.txt'):
            file_path = os.path.join(src_dir, file_name)
            with open(file_path, 'r') as f:
                lines = f.readlines()
            with open(file_path, 'w') as f:
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) == 5:
                        class_id = parts[0]
                        x_center = float(parts[1]) / image_width
                        y_center = float(parts[2]) / image_height
                        width = float(parts[3]) / image_width
                        height = float(parts[4]) / image_height
                        new_line = f"{class_id} {x_center} {y_center} {width} {height}\n"
                        f.write(new_line)
                    else:
                        print(f"Skipping line: {line.strip()} in file {file_name}")

# 修改train目录下的标签文件
modify_labels(os.path.join(label_dir, 'train'))
# 修改val目录下的标签文件
modify_labels(os.path.join(label_dir, 'val'))
# 修改test目录下的标签文件
modify_labels(os.path.join(label_dir, 'test'))