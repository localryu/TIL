import os
import glob
import cv2
import shutil
import sys

ext = ".txt"

# path = sys.argv[1]

path = "/home/ryu/catkin_ws/src/darknet_ros/darknet/data/cam1_label/"
save_path = "/home/ryu/catkin_ws/src/darknet_ros/darknet/data/"
label_path = os.path.join(path,"labels")
img_path = os.path.join(path,"JPEGImages")


f = open(os.path.join(save_path, "train.txt"), 'a')

label_list = os.listdir(label_path)
label_list_ext = [file for file in label_list if file.endswith(ext)]
label_list_ext.sort()

def copy_files(path, ori_filename, save_path, save_filename, ext):
	path_ = os.path.join(path,ori_filename+ext)
	save_path_ = os.path.join(save_path,save_filename+ext)
	shutil.copy(path_, save_path_)

for num, label_file in enumerate(label_list_ext):
	
	filename = label_file[:-4]
	f1 = open(os.path.join(label_path, label_file), 'r')
	line = f1.readline()
	f1.close()
#	if (len(line) == 0):
#		print(filename)
#		continue
	if (filename == "classes"):
		print(filename)
		continue
	
	data = os.path.join(os.path.join(os.getcwd(),img_path),filename+".jpg")+"\n"
	f.write(data)
	
f.close()

copy_files(save_path, "train", save_path, "test",".txt")
