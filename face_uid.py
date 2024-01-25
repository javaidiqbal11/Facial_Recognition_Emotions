import uuid
# from face_app import face_recognition

# Create an empty dictionary to store person IDs and names
person_dict = {}

def create_unique_id():
    """
    Generate a unique ID using the uuid module.
    """
    return str(uuid.uuid4())

# Example usage:
while True:
    # Assume face detection and recognition code returns a name when a new person is detected
    name = face_recognition()
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
            person_id = input(f"Please enter your ID, {name}: ")
            person_dict[name] = person_id
            if not person_id:
                # If the person enters an empty ID, generate a unique ID and store it in the dictionary
                person_id = create_unique_id()
                person_dict[name] = person_id
            print(f"Person: {name}, ID: {person_id}")
