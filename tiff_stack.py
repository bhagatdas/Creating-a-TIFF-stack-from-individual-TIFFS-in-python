import glob
import tifffile as tf
from pystackreg import StackReg
from skimage import io
from matplotlib import pyplot as plt
import numpy as np
import os

path = os.getcwd()
data_names = list(os.listdir(path))
output_path = os.path.join(path,'output')

if not os.path.exists(output_path):
        os.makedirs(output_path)

folders = []
for data in data_names:
    if data == 'preprocess.py' or data == 'output':
        continue
    else:
        folders.append(data)
print(folders)

total_folder_path = []
for folder in folders:
     total_folder_path.append(os.path.join(path,folder))

print(total_folder_path)

total_output_path = []
for folder in folders:
     total_output_path.append(os.path.join(output_path,folder))
     if not os.path.exists(os.path.join(output_path,folder)):
        os.makedirs(os.path.join(output_path,folder))

print(total_output_path)
# total_folder_path = total_folder_path.sort()
# total_output_path = total_output_path.sort()

tile = ['Tiles 1', 'Tiles 2','Tiles 3', 'Tiles 4','Tiles 5', 'Tiles 6']
for i in range(len(total_folder_path)):
    for t in range(len(tile)):
        with tf.TiffWriter(os.path.join(total_output_path[i],'image'+str(t+1)+'.tif')) as stack:   #change name
            for filename in glob.glob(os.path.join(total_folder_path[i],tile[t],'*')):
                stack.save(
                    tf.imread(filename), 
                    photometric='minisblack', 
                    contiguous=True
                )

        # print(os.path.join(total_output_path[i],'image'+str(t)+'.tif'))
        # print(os.path.join(total_folder_path[i],tile[t],'*'))
        
        image = tf.imread(os.path.join(total_output_path[i],'image'+str(t+1)+'.tif'))  #change name
        image = np.transpose(image, axes=(1, 2, 0))
        print(image.shape)
        tf.imsave(os.path.join(total_output_path[i],'image'+str(t+1)+'.tif'),image)     #change name

print("DONE PRINTING")
