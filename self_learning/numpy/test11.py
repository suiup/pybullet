import numpy as np

a=np.linspace(-1,1,5)

b=np.linspace(-1,1,5)

print("a: ",a)

print("b: ", b)

x,y=np.meshgrid(a,b)
print("x: ",x)
print("y: ",y)
z=x**2-y**2
print("z: ",z)
