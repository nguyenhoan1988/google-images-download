"""
  2021/10/8 RaijinCheng:
    * While you are using lateset Pixellib, please make sure
        1. keras version is 2.0.8
        2. h5py version is 2.10.0e
      otherwise the object detection will be unreasonable lines
    * For mask_rcnn_coco.h, please download it from https://github.com/matterport/Mask_RCNN/releases
    * Please note that I already modify segment_image.segmentImage in order to separate different extrections
        You can refer my github https://github.com/RaijinCheng/PixelLib

"""

import datetime
import os
import pixellib
from pixellib.instance import instance_segmentation

#change folder
os.chdir("D:\\AI_Garbage\\Training_Data")

#Load CoCo Dataset
segment_image=instance_segmentation()
segment_image.load_model("mask_rcnn_coco.h5")

#Change to re-think folder
os.chdir("D:\\AI_Garbage\\Training_Data\\re-think")

#for each sub-folders, run object detection and segmentation to genereate Training materials
for directory in os.listdir("D:\\AI_Garbage\\Training_Data\\re-think"):
    os.chdir("D:\\AI_Garbage\\Training_Data\\re-think\\" + directory)
    for full_name in os.listdir("D:\\AI_Garbage\\Training_Data\\re-think\\" + directory):
        print(datetime.datetime.now())
        print("D:\\AI_Garbage\\Training_Data\\re-think\\" + directory)
        print(full_name)
        filename, extension= os.path.splitext(full_name)
        segment_image.segmentImage(full_name, extract_segmented_objects=True,
                        save_extracted_objects=True, save_extracted_objects_name=filename + "_" + extension, show_bboxes=True,
                        output_image_name= filename + "_" + extension + "_output.jpg")

"""
For Video extraction
import pixellib
from pixellib.instance import instance_segmentation

segment_video = instance_segmentation()
segment_video.load_model("mask_rcnn_coco.h5")
segment_video.process_video("sample.mp4", show_bboxes=True,  extract_segmented_objects=True,
save_extracted_objects=True, frames_per_second= 5,  output_video_name="output.mp4")
"""