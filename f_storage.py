'''
I load the images that are in the database_images folder
'''
import config as cfg
import os
import f_main
import cv2
import numpy as np
import traceback


def load_images_to_database():
    list_images = os.listdir(cfg.path_images)
    # filter files that are not images
    list_images = [File for File in list_images if File.endswith(('.jpg','.jpeg','JPEG'))]

    # initialize variables
    name = []
    Feats = []

    # image ingestion
    for file_name in list_images:
        im = cv2.imread(cfg.path_images+os.sep+file_name)

        # I get the features of the face
        box_face = f_main.rec_face.detect_face(im)
        feat = f_main.rec_face.get_features(im,box_face)
        if len(feat)!=1:
            '''
            
            This means that there are no faces or there is more than one face.
            '''
            continue
        else:
            # I insert the new features into the database
            new_name = file_name.split(".")[0]
            if new_name == "":
                continue
            name.append(new_name)
            if len(Feats)==0:
                Feats = np.frombuffer(feat[0], dtype=np.float64)
            else:
                Feats = np.vstack((Feats,np.frombuffer(feat[0], dtype=np.float64)))
    return name, Feats