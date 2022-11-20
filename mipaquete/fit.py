from mipaquete.data import fetch_data , preprocess_data , split_data
from mipaquete.model import pipeline
from mipaquete.export  import save_pickle
                     
                     
def main ( ) :
    print ( " Entrenando modelo del titanic y exportando pickle ... FITTTT " )
    X , y = fetch_data( )
    X = preprocess_data( X )
    X_train , X_test , y_train , y_test = split_data ( X , y )
    
    pipeline.fit ( X_train , y_train )
    
    save_pickle ( pipeline , " titanic.pkl " )
   
if __name__ == '__main__':
    main()


# from mipaquete.data import fetch_data, preprocess_data, split_data

# def main():
#     print('Entrenando modelo del titanic')
#     X, y = fetch_data()
#     X = preprocess_data(X) 


#     X_train, X_test, y_train, y_test = spli
