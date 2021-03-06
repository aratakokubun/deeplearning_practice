# -*- coding:utf-8 -*-

# imports
import numpy as np

def AND_org(x1, x2):
	w1, w2, theta = 0.5, 0.5, 0.7;
	tmp = x1*w1 + x2*w2;
	if tmp <= theta:
		return 0;
	else:
		return 1;

def AND(x1, x2):
	w = np.array([0.5, 0.5])
	x = np.array([x1, x2])
	b = -0.7
	if np.sum(w*x) + b <= 0:
		return 0
	else:
		return 1

def NAND(x1, x2):
	w = np.array([-0.5, -0.5])
	x = np.array([x1, x2])
	b = 0.7
	if np.sum(w*x) + b <= 0:
		return 0
	else:
		return 1

def OR(x1, x2):
	w = np.array([0.5, 0.5])
	x = np.array([x1, x2])
	b = -0.2
	if np.sum(w*x) + b <= 0:
		return 0
	else:
		return 1

def XOR(x1, x2):
	s1 = NAND(x1, x2)
	s2 = OR(x1, x2)
	y = AND(s1, s2)
	return y
