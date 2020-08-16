import numpy as np
import arr
import TrainAndCheck


def load_from_file():
    return np.load('C:\Users\MJay\PycharmProjects\\backpropogation\\w1.npy'), np.load('C:\Users\MJay\PycharmProjects\\backpropogation\\b1.npy'), np.load('C:\Users\MJay\PycharmProjects\\backpropogation\\b2.npy'), np.load('C:\Users\MJay\PycharmProjects\\backpropogation\\w2.npy')


def test_data(input_mat):
    w1, b1, b2, w2 = load_from_file()

    first_half=arr.forward_prop(input_mat[0],w1,b1)
    first_half=arr.activation(first_half)
    second_half=arr.forward_prop(first_half,w2,b2)
    second_half=arr.activation(second_half)

    return TrainAndCheck.parse_result(second_half)