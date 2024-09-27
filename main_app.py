# main code fiel to perform the facial recognition
import os
import uuid
import shutil
from recognizer import face_recognizer
from create_classifier import train_classifer
from create_dataset import start_capture

name = input(f"Please enter your name!")
input_id = input(f"Please enter your ID!")

person_dict = {}

def create_unique_id():
    """
    Generate a unique ID using the uuid module.
    """
    return str(uuid.uuid4())

def face_recognition(username):
    if os.path.exists("data/{}".format(username)):
        face_recognizer(username)

        print("Person recognized as: {}".format(username))
        # input('Press Enter to Exit...')

    if not os.path.exists("data/classifiers/{}_classifier.xml".format(username)):
        start_capture(username)
        train_classifer(username)

    if os.path.exists("data/{}".format(username)):
        shutil.rmtree("data/{}".format(username))

    # if face_recognizer(username):
    #     print("Person recognized as: {}".format(username))
    #     input('Press Enter to Exit...')
    # else:
    #     print("Unknown face")
    #     input('Press Enter to Exit...')

    if name is not None:
        # Check if the person is already in the dictionary
        if name in person_dict:
            person_id = person_dict[name]
            # Ask the person to enter their ID to validate their identity
            input_id = input(f"Please enter your ID, {name}: ")
            if input_id == person_id:
                print(f"Person: {name}, ID: {person_id}, Identity validated!")
            else:
                print(f"Person: {name}, ID: {person_id}, Invalid identity!")
        else:
            # If the person is new, allow them to enter their own ID and store it in the dictionary
            person_id = input(f"Please enter your ID for Validation, {name}: ")
            person_dict[name] = person_id
            if not person_id:
                # If the person enters an empty ID, generate a unique ID and store it in the dictionary
                person_id = create_unique_id()
                person_dict[name] = person_id

                face_recognizer(username)
            print(f"Person: {name}, ID: {person_id}")



face_recognition(name)
