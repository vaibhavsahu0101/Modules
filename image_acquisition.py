import cv2
import os, os.path
import numpy as np
import image_preprocessing as ip
from models import model
from tensorflow.keras import models
#taking training directory path as user input
train_dir= input("Enter training directory path:")

# Define the image directory path
train_image_dir= train_dir + "images"
train_masks_dir= train_dir + "masks"

image_path_list=[]
valid_image_extensions = [".jpg",".jpeg",".png",".tif",".tiff"]
valid_image_extensions = [item.lower() for item in valid_image_extensions]


if not os.path.isdir(train_image_dir):
    quit("The directory {} don't exist !".format(train_image_dir))
if not os.path.isdir(train_masks_dir):
    quit("The directory {} don't exist !".format(train_masks_dir))

for file in os.listdir(train_image_dir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(train_image_dir, file))

if (len(image_path_list) < 150):
    do_augmentation = True
elif (len(image_path_list) >= 150):
    do_aumentation = input("Would you like to perform image Augmentation: True/False")

if image_path_list is None:
    quit("No file in {} !".format(train_images_dir))

tab_images=[]
tab_masks=[]
train_dataset=[]
train_dataset=[]

for file in image_path_list:

    image_original = cv2.imread(file)
    tab_iamges.append(image_original)
    file_name = file.split('.')[0]
    extension_ = file.split('.')[1]
    mask_file = train_masks_dir + file_name + extension_
    mask_original = cv2.imread(mask_file)
    tab_masks.append(mask_original)

    if do_augmentation:
        image_aug, mask_aug = ip.convert(image_original, mask__original)
        image_aug, mask_aug = ip.augment(image_aug, mask_aug)
        tab_images.append(image_aug)
        tab_masks.append(mask_aug)

        train_dataset.append(image_original, mask__original)
