import pickle


def make_pickler(data, filename):            
    return pickle.dump(data, open("save.p", "wb"))
    
    
def unpickler(filename):
    to_be_unpickled = pickle.load(open ("save.p", "rb"))
    return to_be_unpickled
    
    
    

    