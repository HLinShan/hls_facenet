
#用来计算两张人脸图像之间的距离矩阵。需要输入的参数：
#预训练模型 用image_dir文件夹底下 左右人脸去做特征对比，构成矩阵
# 输入的是一个整个的文件夹 E:\dection_py\understand_facenet-master\understand_facenet\align\data\ls_face
# 里面有20+的子文件代表一个类，子文件夹底下又有无数张个人照片，希望相应抽取每个类，每张图片的feature。

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
import matplotlib.pyplot as plt

flags = tf.flags
flags.DEFINE_string("model", "20180402-114759", "data input")
flags.DEFINE_string("image_dir", "./compare_faces", "data out_put")
flags.DEFINE_integer('image_size', 160,'image_size')
flags.DEFINE_integer('margin', 32, 'the margin')
flags.DEFINE_float('gpu_memory_fraction',1.0,  ' ')
flags.DEFINE_boolean('detect_multiple_faces', False, 'True for train, else test. [True]')
flags.DEFINE_boolean('random_order', False, 'True for train, else test. [True]')
FLAGS = flags.FLAGS

def main():
    print(FLAGS.image_dir)
    image_files=[]
    for file in os.listdir(FLAGS.image_dir):
        image_files.append(os.path.join(FLAGS.image_dir,file))

    images = load_and_align_data(image_files, FLAGS.image_size, FLAGS.margin, FLAGS.gpu_memory_fraction)
    # plt.figure()
    # plt.imshow(images[1,:])
    # plt.show()
    # print('askhnauisd')

    with tf.Graph().as_default():

        with tf.Session() as sess:
      
            # Load the model
            facenet.load_model(FLAGS.model)
    
            # Get input and output tensors
            images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            # print("embeddings",embeddings.eval())
            # print(embeddings.data)


            phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")

            print("image",images)
            # Run forward pass to calculate embeddings
            feed_dict = { images_placeholder: images, phase_train_placeholder:False }

            emb = sess.run(embeddings, feed_dict=feed_dict)
            print(emb)

            nrof_images = len(image_files)

            print('Images:')
            for i in range(nrof_images):
                print('%1d: %s' % (i, image_files[i]))
            print('')
            
            # Print distance matrix
            print('Distance matrix')
            print('    ', end='')
            for i in range(nrof_images):
                print('    %1d     ' % i, end='')
            print('')
            for i in range(nrof_images):
                print('%1d  ' % i, end='')
                for j in range(nrof_images):
                    dist = np.sqrt(np.sum(np.square(np.subtract(emb[i,:], emb[j,:]))))
                    print('  %1.4f  ' % dist, end='')
                print('')


# image_paths
# image_size
# margin
# gpu_memory_fraction
def load_and_align_data(image_paths, image_size, margin, gpu_memory_fraction):

    minsize = 20 # minimum size of face
    threshold = [ 0.6, 0.7, 0.7 ]  # three steps's threshold
    factor = 0.709 # scale factor
    
    print('Creating networks and loading parameters')
    with tf.Graph().as_default():
        gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=gpu_memory_fraction)
        sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
        with sess.as_default():
            pnet, rnet, onet = align.detect_face.create_mtcnn(sess, None)
            # pnet, rnet, net = detect_face.create_mtcnn(sess, None)

    tmp_image_paths = image_paths.copy()
    img_list = []
    for image in tmp_image_paths:
        img = misc.imread(os.path.expanduser(image), mode='RGB')
        img_size = np.asarray(img.shape)[0:2]

        # # 图片人脸对齐检测人脸，将mtcnn之后的文件夹送入，即不需要做这个操作
        # bounding_boxes, _ = align.detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)

        # bounding_boxes, _ = detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)

        # if len(bounding_boxes) < 1:
        #   image_paths.remove(image)
        #   print("can't detect face, remove ", image)
        #   continue
        # det = np.squeeze(bounding_boxes[0,0:4])  #去掉了最后一个元素？
        # bb = np.zeros(4, dtype=np.int32)
        # # np.maximum：(X, Y, out=None) ，X 与 Y 逐位比较取其大者；相当于矩阵个元素比较
        # bb[0] = np.maximum(det[0]-margin/2, 0)#margin：人脸的宽和高？默认为44
        # bb[1] = np.maximum(det[1]-margin/2, 0)
        # bb[2] = np.minimum(det[2]+margin/2, img_size[1])
        # bb[3] = np.minimum(det[3]+margin/2, img_size[0])
        # cropped = img[bb[1]:bb[3],bb[0]:bb[2],:]

        cropped = img
        aligned = misc.imresize(cropped, (image_size, image_size), interp='bilinear')
        prewhitened = facenet.prewhiten(aligned)
        img_list.append(prewhitened)
    images = np.stack(img_list)
    return images
    # return img

# def parse_arguments():
#     parser = argparse.ArgumentParser()
#
#     parser.add_argument('model', type=str,
#         help='Could be either a directory containing the meta_file and ckpt_file or a model protobuf (.pb) file',default="20180402-114759")
#     parser.add_argument('image_files', type=str, nargs='+', help='Images to compare')
#     parser.add_argument('--image_size', type=int,
#         help='Image size (height, width) in pixels.', default=160)
#     parser.add_argument('--margin', type=int,
#         help='Margin for the crop around the bounding box (height, width) in pixels.', default=44)
#     parser.add_argument('--gpu_memory_fraction', type=float,
#         help='Upper bound on the amount of GPU memory that will be used by the process.', default=1.0)
#     return parser.parse_args()



if __name__ == '__main__':
    #这是一个从外部输入参数的代码。
    main()
