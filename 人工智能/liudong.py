import time
import numpy as np
import random

def run(*p):
	start = time.time()
	method = p[0]
	params = p[1:]
	method(params)
	print("%s 运行时间：%f"%(method.__name__, time.time() - start))


def avg1(p):
	n = 0
	arr = []
	while n < p[0]:
		arr.append(random.random())
		n += 1
	return sum(arr) / len(arr)

def avg2(p):
	arr = np.random.random(p[0])
	return np.mean(arr)

def new_arrs1(p):
	arrs = []
	x_ = 0
	y_ = 0
	while x_ < p[0]:
		x_ += 1
		arr = []
		while y_ < p[1]:
			y_ += 1
			arr.append(1)
		y_ = 0
		arrs.append(arr)
	a = np.array(arrs)
	print(a.shape)
	return arrs

def new_arrs2(p):
	a = np.full((p[0],p[1]), 1)
	print(a.shape)


# run(avg1, 10000000)
# run(avg2, 10000000)
run(new_arrs1, 3000, 3000)
run(new_arrs2, 30000, 30from torchvision import datasets,transforms000)


