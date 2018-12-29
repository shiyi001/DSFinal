import random
import os
import cv2
import shutil

img_lists = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

# make val dir
if os.path.exists("val"):
    shutil.rmtree("val")
    os.mkdir("val")

for img_list in img_lists:
    # make flower dirs
    val_img_dir = os.path.join("val", img_list)
    os.mkdir(val_img_dir)

    for root, dirs, files in os.walk(os.path.join('train', img_list)):
        for file_name in files:
            if (random.random() > 0.9):
                ori_img_path = os.path.join(root, file_name)
                new_img_path = ori_img_path.replace("train", "val")

                img = cv2.imread(ori_img_path)
                cv2.imwrite(new_img_path, img)
                os.remove(ori_img_path)
                # print (ori_img_path)
                # print (new_img_path)
