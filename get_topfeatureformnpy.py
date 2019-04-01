# encoding:utf-8
# 将输入文件夹中的子文件名字代表每个类，然后将里面所有图片抽取feature 然后保存在npy，做特征底库
# 用来与输入的的人做特征对比选
# 2*512 npy格式
# np文件库中挨个与单独的一个npy 一个人一个feature 进行比较
# 获取每个人与验证的那个人最的那个欧式距离一个人一个值
# {"guagnxiaotong":0.05,"xxx":0.85} 按value值进行小到大排序



from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from scipy import misc
import tensorflow as tf

import numpy as np
import sys
import os
import argparse
import facenet
import align.detect_face
# import detect_face
from PIL import Image
import random
import matplotlib.pyplot as plt
import csv

flags = tf.flags
flags.DEFINE_string("npy_dir", "./align/data/npy", "data out_put")
flags.DEFINE_string("npy_text", "./align/data/周迅text.npy", "data out_put")
FLAGS = flags.FLAGS


def main():
    #
    npy_files=[]
    dis_map={}
    text_npy=np.load(FLAGS.npy_text)
    print(text_npy.shape)

    for file in os.listdir(FLAGS.npy_dir):
        print(file)
        current_npy=np.load(os.path.join(FLAGS.npy_dir,file))
        min=10
        for j in range(len(current_npy)):
            one_dist = np.linalg.norm(current_npy[j,:] - text_npy)
            if one_dist<min:
                min=one_dist

        dis_map[file.split('.')[0]] = min

    print(dis_map)
    print(sorted(dis_map.items(),key=lambda x:x[1])[0:5])


if __name__ == '__main__':

    main()
