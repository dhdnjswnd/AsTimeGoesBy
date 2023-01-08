# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 23:15:07 2022

@author: dhdnj
"""
import re
import math
import cv2
import numpy as np
import os


input_path = "./2021/"
input_extension = "jpg"
output_path = "./output/"
output_file = "2021.avi"

paths = [os.path.join(input_path, i) for i in os.listdir(input_path) if re.search(".jpg$", i)]
# input_path = "./2022/"
# paths2 = [os.path.join(input_path, i) for i in os.listdir(input_path) if re.search(".jpg$", i)]
# paths = paths + paths2

print(len(paths))
width = 1200
height = 1600
img_array = []
print(paths)

textSize = cv2.getTextSize(paths[0][7:15], fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, thickness=3)

for filename in paths:
    img = cv2.imread(filename)  ## 이미지 파일 불러오기
    img = cv2.resize(img, dsize=(width, height), interpolation=cv2.INTER_AREA) ## 이미지 사이즈 수정.
    cv2.putText(img, filename[7:15], (math.ceil((width-textSize[0][0])/2), height-160), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 100), 3)
    w, h, layer = img.shape
    size = (w, h)
    img_array.append(img)

fps = 10
out = cv2.VideoWriter(output_path + output_file, cv2.VideoWriter_fourcc(*'MJPG'), fps, (width, height))
for i in img_array:
    out.write(i)

out.release()
print(output_path + output_file + '완성')


def __main__():
    print("main")
