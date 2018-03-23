#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 10:18:57 2018

@author: Daniel Yang, Ph.D. (daniel.yj.yang@gmail.com)


MIT License

Copyright (c) 2018 YJ Daniel Yang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import numpy as np
from scipy.spatial import distance


# also known as L2 norm/distance
def Euclidean_dist(p1, p2):
    return np.sqrt(np.sum((p1-p2)**2))


point1 = np.array([1, 2, 3])
point2 = np.array([4, 5, 6])

# Euclidean distance
Euclidean_dist_np = np.linalg.norm(point1-point2, ord=2) # L2 norm
Euclidean_dist_sp = distance.euclidean(point1, point2)  # slower than numpy (twice as slower)
Euclidean_dist = Euclidean_dist(point1, point2)
print(Euclidean_dist_np, Euclidean_dist_sp, Euclidean_dist)


# L1 norm
L1_dist_np = np.linalg.norm(point1-point2, ord=1) # L1 norm
print(L1_dist_np)