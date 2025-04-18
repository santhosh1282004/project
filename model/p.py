
import numpy as np
import pickle
def heartDiseasePredusion():
  with open(r"S:\project\heartDiseasePredusion.pkl",'rb') as file:
    model=pickle.load(file)
  inpot=[63,1,3,145,233,1,0,140,0,2.3,2,0,1]
  array=np.asarray(inpot)
  array_reshape=array.reshape(1,-1)
  pred=model.predict(array_reshape)
  print(pred)
heartDiseasePredusion()
def LungCancer():
  with open("LungCancer.pkl",'rb') as file:
    model=pickle.load(file)
    inpot=(0,69,1,2,2,1,1,2,1,2,2,2,2,2)
    array=np.asarray(inpot)
    array_re=array.reshape(1,-1)
    pred=model.predict(array_re)
    print(pred)
LungCancer()
def diabetes():
  with open("diabetes.pkl",'rb') as file:
    model=pickle.load(file)
    inpot=(6,148,72,35,0,33.6,0.627,50)
    array=np.asarray(inpot)
    array_re=array.reshape(1,-1)
    pred=model.predict(array_re)
    print(pred)
diabetes()
    