from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Create an empty dictionary to store the arrays and user IDs
storage = {}

@app.route('/store', methods=['POST'])
def store_array():
    """
    Endpoint to store a NumPy array and user ID.
    Expects a JSON payload with the following format:
    {
        "user_id": <string>,
        "data": <array>
    }
    """
    req_data = request.get_json()

    # Extract the user ID and array from the request data
    user_id = req_data.get('user_id')
    array_data = req_data.get('data')

    # Convert the array data to a NumPy array
    array = np.array(array_data)

    # Store the array and user ID in the dictionary
    storage[user_id] = array

    return jsonify({'message': 'Array stored successfully.'}), 200

@app.route('/retrieve/<user_id>', methods=['GET'])
def retrieve_array(user_id):
    """
    Endpoint to retrieve a stored NumPy array by user ID.
    """
    if user_id not in storage:
        return jsonify({'error': 'User ID not found.'}), 404

    # Retrieve the array from the dictionary and convert it to a list
    array = storage[user_id]
    array_list = array.tolist()

    return jsonify({'data': array_list}), 200

if __name__ == '__main__':
    app.run(debug=True)
