import numpy as np

def getRotX(degree, unit='rad'):
    if(unit=='deg'):
        degree = np.radians(degree)
    elif(unit!='rad'):
        raise ValueError("The unit was different from \'rad\' or \'deg\'")
    
    T = np.array([[1., 0.,              0.,               0.],
                 [0., np.cos(degree), -np.sin(degree), 0.],
                 [0., np.sin(degree), np.cos(degree),  0.],
                 [0., 0.,              0.,               1.]])
    return T

def getRotY(degree, unit='rad'):
    if(unit=='deg'):
        degree = np.radians(degree)
    elif(unit!='rad'):
        raise ValueError("The unit was different from \'rad\' or \'deg\'")
    
    T = np.array([[np.cos(degree), 0.,np.sin(degree),0.],
                 [0., 1., 0., 0.],
                 [-np.sin(degree), 0., np.cos(degree),  0.],
                 [0., 0.,              0.,               1.]])
    return T

def getRotZ(degree, unit='rad'):
    if(unit=='deg'):
        degree = np.radians(degree)
    elif(unit!='rad'):
        raise ValueError("The unit was different from \'rad\' or \'deg\'")
    
    T = np.array([np.cos(degree), -np.sin(degree),0.,0.],
                 [np.sin(degree), np.cos(degree),0.,0.],
                 [0.,0.,1.,0.],
                 [0.,0.,0.,1.])
    return T

# Aindan sei como concatena essas matrizes
def getTrans(trans):
    T = np.array([np.cos(degree), -np.sin(degree),0.,0.],
                 [np.sin(degree), np.cos(degree),0.,0.],
                 [0.,0.,1.,0.],
                 [0.,0.,0.,1.])
    return T


P = np.array([[3,2,1.,1.]]).transpose()

print("P\n",P.shape,"\n")

print("T\n",getRotX(45,"deg"),"\n")


print("T(45)*P\n",getRotX(45,"deg")@P,"\n")

trans1 = np.array([[1.,0. ,0.,1.],
                  [0.,1.,0.,2],
                  [0.,0.,1.,3],
                  [0.,0.,0.,1.]])
print("trans(1.23)T(45)P\n",trans1@getRotX(45,"deg")@P,"\n")

print("T(60.)trans(1.23)T(45)P\n",getRotY(60.,"deg")@trans1@getRotX(45,"deg")@P,"\n")

trans2 = np.array([[1.,0. ,0.,-1.],
                  [0,1,0.,-3],
                  [0.,0.,1.,-1.],
                  [0.,0.,0.,1.]])
print("trans(-1.,-3,-1.)T(60.)trans(1.23)T(45)P\n",trans2@getRotY(60.,"deg")@trans1@getRotX(45,"deg")@P,"\n")
