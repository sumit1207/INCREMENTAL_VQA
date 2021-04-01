import numpy as np


data =np.load('queation_feature.npz')
rf1=data['name1']
rf2=data['name2']
print(rf1.shape,rf2.shape)