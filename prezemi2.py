print('a(1,2,3,4)とb(4,3,2,1)のユークリッド距離を求めます。')



import numpy as np

a = np.array((1,2,3,4))
b = np.array((4,3,2,1))

dist = np.linalg.norm(a-b)

print(dist)

