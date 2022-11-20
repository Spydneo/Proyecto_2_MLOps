import pickle

def save_pickle(model, filename):
    with open(filename, 'wb') as f:
        pickle.dump(model, f)