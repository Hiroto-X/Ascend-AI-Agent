def success(data=None):
    return {"ok":True,"data":data,"error":None}

def failure(error):
    return {"ok":False,"data":None,"error":str(error)}