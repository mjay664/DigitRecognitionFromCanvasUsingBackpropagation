import numpy as np
import random
from math import exp
'''
input_mat=np.load('Final_ip.npy')
output_mat=np.load('Final_op.npy')
b1=np.random.rand(1024)
b2=[0.3,0.4,0.3,.22]
print(output_mat)
w1=np.random.randint(-1,2,(1024,1024))
w2=np.random.randint(-1,2,(1024,4))
'''
eta=.05

def update_w2(m,e):
    e=e*eta

    m=m.reshape((-1,1))
   # print("value of: ", e)
    e = e.reshape((1, 4))
    m=np.dot(m,e)
    return (w2+m)


def error_hidden(op,summ):
    return op*(1-op)*summ


def activation(mat):
    x=mat.shape
  #  print("value of x: ",x)
    for i in range(0,x[0]):
        mat[i]=1/(1+exp(-mat[i]))
    return mat

def forward_prop(input_mat,w,b):
    l=np.dot(input_mat,w)
    return l+b

def oplayer_err(cal,op):
    err=cal*(1-cal)*(op-cal)
    return err

'''
for k in range(0,1000):
    for i in range(0,2260):
        first_half=forward_prop(input_mat[i],w1,b1)
        first_half=activation(first_half)
        second_half=forward_prop(first_half,w2,b2)
        second_half=activation(second_half)
            #print(second_half)
        error_op=oplayer_err(second_half,output_mat[i])
        sub=w2*error_op#individual elements are multiplied
        sub=sub.sum(axis=1)#will give a row matrix which contains column sum i.e a[0][0]+a[0][1].....
        error_hidd=error_hidden(first_half,sub)
        w2=update_w2(first_half,error_op)
        deltaw1=input_mat[i]*error_hidd*eta
        w1=w1+deltaw1
        b2=b2+eta*error_op
        b1=b1+eta*error_hidd
    print(k)

np.save('w1',w1)
np.save('w2',w2)
np.save('b1',b1)
np.save('b2',b2)
'''
#testing the weight matrix




