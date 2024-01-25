import cv2
import os
import numpy as np
from PIL import Image


def train_classifer(name):
    path = os.path.join(os.getcwd() + "/data/" + name + "/")
    faces = []
    ids = []
    pictures = {}

    for root, dirs, files in os.walk(path):
        pictures = files

    for pic in pictures:
        imgpath = path + pic
        img = Image.open(imgpath).convert('L')
        imageNp = np.array(img, 'uint8')
        id = int(pic.split(name)[0])
        # names[name].append(id)
        faces.append(imageNp)
        ids.append(id)

    ids = np.array(ids)

    clf = cv2.face.LBPHFaceRecognizer_create()

    clf.train(faces, ids)
    clf.write("./data/classifiers/" + name + "_classifier.xml")
