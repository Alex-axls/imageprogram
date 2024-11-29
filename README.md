给已经有的PPI图像打上标记，用YOLO网络来检测出目标
把雷达学报PPI的bmp转成pnghttps://mp.weixin.qq.com/s/iOppHql3zDXiGFY_Alh9oA,裁剪重点区域https://mp.weixin.qq.com/s/pPZoYya1t-KkGUymWLo8Ww
    width_start = width / 2.2
    height_start = height / 3
    rect = (width_start, height_start, width_start+520, height_start+520)

    width_start = width / 2
    height_start = height / 3.5
    root_path = "E:/Data/X_Radar_Data/20200202PPI/Pulse T1-单载频-05"
    save_path = "E:/Data/X_Radar_Data/20200202PPI/crop4"
    width_start = width / 2
    height_start = height / 3.5
    root_path = "E:/Data/X_Radar_Data/20200202PPI/Pulse T1-单载频-04"
    save_path = "E:/Data/X_Radar_Data/20200202PPI/crop4"

https://blog.csdn.net/dally2/article/details/117904166将json文件转化为txt文件
https://blog.csdn.net/m0_63774211/article/details/135271794 划分training val test

配置文件PPI.yaml
train: E:/pythonProject/ultralytics-main/PPI/images/train
val: E:/pythonProject/ultralytics-main/PPI/images/val
test: E:/pythonProject/ultralytics-main/PPI/images/test

name_delmat.py把图片名字.mat.png里面的.mat去掉，使其和标签文件txt的名字匹配

labelme安装，给图片打标签

YOLO期望标签文件的格式是每行包含一个对象的边界框信息，格式如下：
<class_id> <x_center> <y_center> <width> <height>
标签文件路径
而我现有的是：
20200722143125_02_scanning 169.859155 369.507042 26.760563 16.197183
需要改成
0 169.859155 369.507042 26.760563 16.197183
修改jsontxt.py
file_str = '0' + ' ' + str(round(x, 6)) + ' ' + str(round(y, 6)) + ' ' + str(round(w, 6)) + \
               ' ' + str(round(h, 6))
其中<class_id> 是类别编号（整数）。
<x_center> 和 <y_center> 是边界框中心点的相对坐标（相对于图像宽度和高度的比例，范围在0到1之间）。
<width> 和 <height> 是边界框的宽度和高度的相对值（相对于图像宽度和高度的比例，范围在0到1之间）
如果标签文件中的坐标不是相对坐标，需要将其转换为相对坐标。
我的图片是520x520像素的
跑 train.py
跑 detect.py
跑 heatmap.py

魔鬼面具
动手学深度学习-李沐
小土堆pytorch学习
