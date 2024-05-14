# Q2
from sklearn.metrics import confusion_matrix
def prednrecal( cm):
    pred = cm[0][0]/(cm[0][0] + cm[0][1])
    
    recall = cm[0][0]/(cm[0][0] + cm[1][0])
    print(f"Prediction : {pred}")
    print(f"Recall : {recall}")
    
actual =[0,1,0,1,1,0,1,0]
prediction = [0,1,1,0,0,0,0,0]

Cm = confusion_matrix(actual, prediction)
print(Cm)
prednrecal(Cm)