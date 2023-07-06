from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    for i in range(0,480):
        for j in range(0,640):
            if j < 320 and j > 60:
                if i > (1/400)*(j-320)**2 + 130:
                    res[i,j] = 0.20
                if i > (1/400)*(j-320)**2 + 170:
                    res[i,j] = 0.40
                if i > (1/400)*(j-320)**2 + 210:
                    res[i,j] = 0.60
                if i > (1/400)*(j-320)**2 + 250:
                    res[i,j] = 0.80
                if i > (1/400)*(j-320)**2 + 290:
                    res[i,j] = 1.00
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    for i in range(0,480):
        for j in range(0,640):
            if j >= 320 and j < 580:
                if i > (1/400)*(j-320)**2 + 130:
                    res[i,j] = -0.20
                if i > (1/400)*(j-320)**2 + 170:
                    res[i,j] = -0.40
                if i > (1/400)*(j-320)**2 + 210:
                    res[i,j] = -0.60
                if i > (1/400)*(j-320)**2 + 250:
                    res[i,j] = -0.80
                if i > (1/400)*(j-320)**2 + 290:
                    res[i,j] = -1.00
    return res
