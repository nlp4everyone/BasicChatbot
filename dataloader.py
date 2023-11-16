import json

def load_from_path(path:str):
    data = None
    with open(path,'r') as f:
        data = json.load(f)

    if data is None:
        return data

    sentences = []
    labels = []
    data_pairs = data["intent"]
    for data_pair in data_pairs:
        # Add sentence class
        infor = list(data_pair.values())[0]
        sentences.extend(infor["question"])

        # Add key class
        class_name = list(data_pair.keys())
        labels.extend(class_name*len(infor["question"]))
    return sentences,labels
