import pickle
emp = {1:"A",2:"B",3:"C",4:"D",5:"E", 6:"F"}
pickling_on = open("/Users/Shrihan/Desktop/emp.txt","wb")
pickle.dump(emp, pickling_on)
pickling_on.close()
