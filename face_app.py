import os
import shutil
import cv2
from recognizer import face_recognizer
from create_classifier import train_classifer
from create_dataset import start_capture

name = input("Enter your name once! ")


def face_recognition(username):
    if os.path.exists("data/{}".format(username)):
        face_recognizer(username)

        print("Person recognized as: {}".format(username))
        input('Press Enter to Exit...')

    if not os.path.exists("data/classifiers/{}_classifier.xml".format(username)):
        # name = input("Enter your name once! ")
        start_capture(username)
        train_classifer(username)

    if os.path.exists("data/{}".format(username)):
        shutil.rmtree("data/{}".format(username))

    if face_recognizer(username):
        print("Welcome to DoctorAi: {}".format(username))
        input('Press Enter to Exit...')
    else:
        print("Unknown face")
        input('Press Enter to Exit...')


face_recognition(name)
