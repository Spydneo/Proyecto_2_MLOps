from sklearn.datasets import fetch_openml
from random import randint
from sklearn.model_selection import train_test_split

def fetch_data():
    """
    fetch data descarga deopenml eldataset de titanic.
    Devuelve dos Dataframe: X e y
    """
    return fetch_openml("titanic", 
    version=1, 
    as_frame=True, 
    return_X_y=True)



def preprocess_data(X):

    return X.rename(columns={

        "home.dest": "homedest"

    })

# def split_data(X, y):
#     seed = randint()
#     return train_test_split(X, y, test_size=0.2)



def split_data(X, y):

    seed = randint(0,10000000)    

    return train_test_split(X, y, test_size=0.2, random_state=seed)