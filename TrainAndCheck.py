import numpy as np
import math
import DataHelper as data_set_class
import weights_two_testing


def weight_matrix(no_inputs, no_outputs):
    hidden_layer_weights = np.random.rand(no_inputs, no_inputs)
    bias_1 = np.random.rand(no_inputs)
    bias_2 = np.random.rand(no_outputs)
    output_layer_weights = np.random.rand(no_inputs, no_outputs)

    return hidden_layer_weights, bias_1, output_layer_weights, bias_2


def weight_matrix_2(no_inputs, no_outputs):
    hidden_layer_weights = np.array(np.random.randint(-1, 2, (no_inputs, no_inputs)), dtype=float)
    bias_1 = np.array(np.random.randint(-1, 2, (no_inputs)), dtype=float)
    bias_2 = np.array(np.random.randint(-1, 2, (no_outputs)), dtype=float)
    output_layer_weights = np.array(np.random.randint(-1, 2, (no_inputs, no_outputs)), dtype=float)
    print 'Weight Matrices Initialized'
    return hidden_layer_weights, bias_1, output_layer_weights, bias_2


def activation_function(value):
    return 1/(1+math.exp(-value))


def forward_propagation(input_mat, weights, bias, flag=False):
    output = np.dot(input_mat, weights)

    output += bias

    tmp = []
    if not flag:
        for i in output:
            tmp.append(activation_function(i))
    else:
        return np.array(output)

    return np.array(tmp)


def transfer_function(output):
    return output * (1 - output)


def output_layer_back_propagation(forward_ops, target_ops):
    err = (target_ops - forward_ops) * transfer_function(forward_ops)

    return err


def hidden_layer_back_propagation(output_weights, op_err, hidden_ops):
    err = transfer_function(hidden_ops)
    tmp = np.dot(output_weights, op_err.transpose())
    err *= tmp
    return err


def get_del_w(op_err, outputs, learning_rate):
    return learning_rate * (outputs * op_err)


def weights_update(output_weights, op_err, outputs, bias, learning_rate):
    for i in range(0, len(output_weights)):
        x = get_del_w(op_err, outputs[i], learning_rate)
        for j in range(len(output_weights[i])):
            output_weights[i][j] += x[j]

    x = get_del_w(op_err, np.array([1]), learning_rate)
    for i in range(len(bias)):
        bias[i] += x[i]

    return output_weights, bias


def load_from_file():
    return np.load('C:\Users\MJay\PycharmProjects\\backpropogation\\hidden1.npy'), np.load('C:\Users\MJay\PycharmProjects\\backpropogation\\b11.npy'), np.load('C:\Users\MJay\PycharmProjects\\backpropogation\\b21.npy'), np.load('C:\Users\MJay\PycharmProjects\\backpropogation\\op1.npy')


def train_network(iterations, input_mat, output_mat, learning_rate):

    h1, b1, b2, ow1 = load_from_file()
    print 'Now Loop '
    k = 0
    while k <= iterations:
        print k
        for i in range(0, len(input_mat)):
            print i
            hidden_ops = forward_propagation(input_mat[i], h1, b1)
            target_ops = forward_propagation(hidden_ops, ow1, b2)

            op_err = output_layer_back_propagation(target_ops, output_mat[i])
            hidden_err = hidden_layer_back_propagation(ow1, op_err, hidden_ops)

            ow1, b2 = weights_update(ow1, op_err, hidden_ops, b2, learning_rate)
            h1, b1 = weights_update(h1, hidden_err, input_mat[i], b1, learning_rate)

        k += 1

    np.save('hidden1', h1)
    np.save('b11', b1)
    np.save('op1', ow1)
    np.save('b21', b2)


def parse_result(result_mat):
    tmp = []
    for i in result_mat:
        if i >= 0.5:
            tmp.append(1)
        else:
            tmp.append(0)

    if tmp[1] == 1 and tmp[0] == 1:
        tmp[0] = 0
    if tmp[0] == 1 and tmp[2] == 1:
        tmp[0] = 0

    tmp.reverse()
    num = 0
    for i in range(len(tmp)):
        num += (tmp[i] * (2 ** i))

    return num


def test_network(input_mat):
    h1, b1, b2, ow1 = load_from_file()
    s = forward_propagation(input_mat[0], h1, b1)

    z = forward_propagation(s, ow1, b2)

    return parse_result(z)


def initiate_operation(train_flag=True, file_name=None):
    if train_flag:
        op, list_l = data_set_class.dataset()
        print 'Data Loaded'
        input_mat = np.array(list_l)
        output_mat = np.array(op)
        learning_rate = 0.05
        train_network(5, input_mat, output_mat, learning_rate)
    else:
        input_data = data_set_class.get_specific_file(file_name)

        num_1 = test_network(input_data)
        num_2 = weights_two_testing.test_data(input_data)

        return num_1, num_2

