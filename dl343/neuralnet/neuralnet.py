# -*- coding:utf-8 -*-

# imports
import numpy as np
import matplotlib.pylab as plt

# Activation functions
def step_function(x):
	"""
	活性化関数としてのステップ関数の実装
	@param {numpy.array} x: 活性判定を行う値
	@return 1: 活性, 0: 非活性
	"""
	return np.array(x > 0, dtype=np.int)

def sigmoid(x):
	"""
	活性化関数としてのsigmoid関数の実装
	@param {numpy.array} x: 活性判定を行う値
	@return 活性値 
	"""
	return 1 / (1 + np.exp(-x))

def relu(x):
	"""
	活性化関数としてのReLU関数の実装
	@param {numpy.array} x: 活性判定を行う値
	@return 活性値
	"""
	return np.maximum(0, x)

def identity_function(x):
	"""
	活性化関数としての恒等関数の実装
	@param {numpy.array} x: 活性判定を行う値
	@return 活性値
	"""
	return x

# 
