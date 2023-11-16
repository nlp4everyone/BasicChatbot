import random

import classifier
import json
def load_data(path):
    with open(path,'r') as f:
        return json.load(f)

all_data = load_data("Data/data.json")

def get_response(query):
    # Make prediction
    _,intent_class = classifier.predict(query)
    # Get class
    intent_class = intent_class[0]
    # Return response
    for data in all_data["intent"]:
        key_data = list(data.keys())[0]
        # Get the right answer
        if key_data == intent_class:
            response = list(data.values())[0]
            response = response['answer']
            # Random result
            response = random.choice(response)
            print(f"Bot: {response}")
            break

while True:
    user_input = input("User: ")
    get_response(user_input)