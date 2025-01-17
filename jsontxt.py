# https://blog.csdn.net/dally2/article/details/117904166将json文件转化为txt文件
import os
import json

json_dir = 'E:/Project/A_X_Radar_Data/20200202PPI/label_json/c15/'  # json文件路径
out_dir = 'E:/Project/A_X_Radar_Data/20200202PPI/label_txt/'  # 输出的 txt 文件路径


def get_json(json_file, filename):
    # 读取 json 文件数据
    with open(json_file, 'r') as load_f:
        content = json.load(load_f)

    # # 循环处理
    tmp = filename
    filename_txt = out_dir + tmp + '.txt'
    # 创建txt文件
    fp = open(filename_txt, mode="w", encoding="utf-8")
    # 将数据写入文件
    # 计算 yolo 数据格式所需要的中心点的 相对 x, y 坐标, w,h 的值
    x = (content["shapes"][0])["points"][0][0]
    y = (content["shapes"][0])["points"][0][1]
    w = (content["shapes"][0])["points"][1][0] - (content["shapes"][0])["points"][0][0]
    h = (content["shapes"][0])["points"][1][1] - (content["shapes"][0])["points"][0][1]
    fp = open(filename_txt, mode="r+", encoding="utf-8")
    file_str = '0' + ' ' + str(round(x, 6)) + ' ' + str(round(y, 6)) + ' ' + str(round(w, 6)) + \
               ' ' + str(round(h, 6))
    line_data = fp.readlines()

    if len(line_data) != 0:
        fp.write('\n' + file_str)
    else:
        fp.write(file_str)
    fp.close()


def main():
    files = os.listdir(json_dir)  # 得到文件夹下的所有文件名称
    s = []
    for file in files:  # 遍历文件夹
        filename = file.split('.')[0]
        # print(tmp)
        get_json(json_dir + file, filename)


if __name__ == '__main__':
    main()