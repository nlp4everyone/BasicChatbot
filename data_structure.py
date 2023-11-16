import json

data = {
    "intent": [
        {
            "greeting": {
                "question": ["Hello","Hi","Nice to see you","Have a good day!"],
                "answer": ["Nice","Good","I'm fine"]
            },
        },
        {
            "farewell":{
                "question":["Goodbye","See you later","See you tomorrow","Bye"],
                "answer":["Bye","See you soon"]
            },
        },
        {
            "name":{
                "question":["What your name?","Can you tell me about your name"],
                "answer":["My name is Phong","Phong is my name"]
            }
        }

    ]
}

with open("Data/data.json",'w') as f:
    json.dump(data,f,indent=3)