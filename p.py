import numpy as np
import pickle
def heartDiseasePredusion():
  with open("heartDiseasePredusion.pkl",'rb') as file:
    model=pickle.load(file)
    inpot=[]
    array=np.asarray(inpot)
    array_reshape=array.reshape(1,-1)
    pred=model.predict(array_reshape)
    print(pred)
heartDiseasePredusion()
# def LungCancer():
#   with open("LungCancer.pkl",'rb') as file:
#     model=pickle.load(file)
#     inpot=()
#     array=np.asarray(inpot)
#     array_re=array.reshape(1,-1)
#     pred=model.predict(array_re)
#     print(pred)
# LungCancer()
# def diabetes():
#   with open("diabetes.pkl",'rb') as file:
#     model=pickle.load(file)
#     inpot=()
#     array=np.asarray(inpot)
#     array_re=array.reshape(1,-1)
#     pred=model.predict(array_re)
#     print(pred)
# diabetes()
    