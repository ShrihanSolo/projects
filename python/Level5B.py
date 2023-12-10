import pickle

pickle_off = open("/Users/Shrihan/Desktop/topickleornottopickle.pickle.txt","rb")
emp = pickle.load(pickle_off)

for line in emp:
    print("".join(k*v for k,v in line))
