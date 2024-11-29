Mark the existing PPI images and use YOLO network to detect the target. 
Convert the bmp of the PPI of the Journal of Radar to png (https://mp.weixin.qq.com/s/iOppHql3zDXiGFY_Alh9oA)
crop the key areas. （https://mp.weixin.qq.com/s/pPZoYya1t-KkGUymWLo8Ww）
    width_start = width / 2.2
    height_start = height / 3
    rect = (width_start, height_start, width_start+520, height_start+520)
    root_path = "E:/Data/X_Radar_Data/20200202PPI/Pulse T1-单载频-01"
    save_path = "E:/Data/X_Radar_Data/20200202PPI/crop"
    width_start = width / 2
    height_start = height / 3.5
    root_path = "E:/Data/X_Radar_Data/20200202PPI/Pulse T1-单载频-05"
    save_path = "E:/Data/X_Radar_Data/20200202PPI/crop4"
    width_start = width / 2
    height_start = height / 3.5
    root_path = "E:/Data/X_Radar_Data/20200202PPI/Pulse T1-单载频-04"
    save_path = "E:/Data/X_Radar_Data/20200202PPI/crop4"

Convert json file to txt file.(https://blog.csdn.net/dally2/article/details/117904166)
Divide training val test. (https://blog.csdn.net/m0_63774211/article/details/135271794)

Configuration filePPI.yaml
train: E:/pythonProject/ultralytics-main/PPI/images/train
val: E:/pythonProject/ultralytics-main/PPI/images/val
test: E:/pythonProject/ultralytics-main/PPI/images/test

name_delmat.py Remove the .mat from the image name .mat.png so that it matches the name of the label file txt

Install labelme and label pictures

YOLO expects the format of the label file to contain the bounding box information of an object per line, in the following format:
<class_id> <x_center> <y_center> <width> <height>
And what I have now is:
20200722143125_02_scanning 169.859155 369.507042 26.760563 16.197183
Need to be changed to:
0 169.859155 369.507042 26.760563 16.197183
Revise jsontxt.py
file_str = '0' + ' ' + str(round(x, 6)) + ' ' + str(round(y, 6)) + ' ' + str(round(w, 6)) + \
               ' ' + str(round(h, 6))
where <class_id> is the class number (integer).
<x_center> and <y_center> are the relative coordinates of the bounding box center point (in proportion to the image width and height, ranging from 0 to 1).
<width> and <height> are relative values ​​of the width and height of the bounding box (relative to the ratio of image width and height, ranging from 0 to 1)
If the coordinates in the label file are not relative coordinates, they need to be converted to relative coordinates. My image is 520x520 pixels.
run train.py
run detect.py
run heatmap.py

魔鬼面具
动手学深度学习-李沐
小土堆pytorch学习
