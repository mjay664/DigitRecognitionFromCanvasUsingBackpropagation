import numpy as np
import cv2


def output_counter(folder_num):
    if folder_num == 0:
        return [0, 0, 0, 0]
    elif folder_num == 1:
        return [0, 0, 0, 1]
    elif folder_num == 2:
        return [0, 0, 1, 0]
    elif folder_num == 3:
        return [0, 0, 1, 1]
    elif folder_num == 4:
        return [0, 1, 0, 0]
    elif folder_num == 5:
        return [0, 1, 0, 1]
    elif folder_num == 6:
        return [0, 1, 1, 0]
    elif folder_num == 7:
        return [0, 1, 1, 1]
    elif folder_num == 8:
        return [1, 0, 0, 0]
    elif folder_num == 9:
        return [1, 0, 0, 1]


def dataset():
    data_set = []
    output_set = []

    im_num = 0
    while im_num <= 20:
        folder_num = 0
        while folder_num < 10:
            img = cv2.imread('Canvas' + str(folder_num) + '/im' + str(im_num) + '.jpg')
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            rt, thr = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

            _, countour, hei = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            countour = countour[0]
            x, y, z, w = cv2.boundingRect(countour)
            thr = thr[y:y + w, x:x + z]

            thr = cv2.resize(thr, (32, 32))

            aa = np.array(thr)
            img_set = []
            for i in xrange(aa.shape[0]):
                for j in xrange(aa.shape[1]):

                    if aa[i][j] == 0:
                        img_set.append(0)
                    else:
                        img_set.append(1)

            data_set.append(img_set)
            output_set.append(output_counter(folder_num))
            folder_num += 1

        im_num += 1

    return output_set, data_set


def get_specific_file(file_name):
    img = cv2.imread(file_name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rt, thr = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    _, countour, hei = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    countour = countour[0]
    x, y, z, w = cv2.boundingRect(countour)
    thr = thr[y:y+w, x:x+z]
    thr = cv2.resize(thr, (32, 32))
    aa = np.array(thr)
    data_set = []
    img_set = []
    for i in xrange(aa.shape[0]):
        for j in xrange(aa.shape[1]):

            if aa[i][j] == 0 or aa[i][j] < 128:
                img_set.append(0)
            else:
                img_set.append(1)

    data_set.append(img_set)
    return data_set

'''
op, list_l = dataset()
print 'Data Loaded'
input_mat = np.array(list_l)
output_mat = np.array(op)

np.save('Final_ip', input_mat)
np.save('Final_op', output_mat)
'''
