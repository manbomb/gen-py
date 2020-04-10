import numpy as np
import random as rd
import itertools as it

def fit_fun_ind(ind):
	indi = ind.copy().astype('float64')
	ret = 0

	for i in range(0, len(ind)):
		indi[i] /= 255
		#print(indi[i])
		ret += (indi[i])**2

	ret = (ret/3)**(1/2)

	return ret

def fit_fun(gen):
	n = len(gen)
	ret = np.zeros(n)
	for i in range(0,n):
		ret[i] = fit_fun_ind(gen[i])
	return ret

def new_gen(n):
	gen = np.zeros([n,3], dtype=int)

	for i, _ in enumerate(gen):
		for j, _ in enumerate(gen[i]):
			gen[i][j] = rd.randint(0,255)

	return gen

def selection(gen,fit,k): # k é a porcentagem de individuos que vao ser selecionados
	if k > 1:
		k = 1

	if k <= 0:
		k = 0

	n = int(k*len(gen))

	if n == 0:
		n = 1

	fit_gen = fit(gen)
	
	ret = np.zeros([n,3], dtype=int)

	for i in range(0,n):
		ret[i] = gen[np.argmax(fit_gen)]
		fit_gen = np.delete(fit_gen, np.argmax(fit_gen))

	return ret

def cross_over(ind):
	if len(ind) > 1:
		ret = ind.copy()

		n = len(ind)
		n = int(((n-1)*(n))/2)

		for i in range(0,n):
			anomalia = rd.randint(0,2)
			#print('anomalia: '+str(anomalia))
			
			ind_a = rd.randint(0,len(ind)-1)
			#print('ind_a: '+str(ind_a))
			
			ind_b = rd.randint(0,len(ind)-1)
			
			while ind_b == ind_a:
				ind_b = rd.randint(0,len(ind)-1)
			#print('ind_b: '+str(ind_b))

			delta = ind[ind_a][anomalia].copy()
			ret[ind_a][anomalia] = ret[ind_b][anomalia]
			ret[ind_b][anomalia] = delta

		return ret
	else:
		return ind

def raffle(k):
	if k > 1:
		k == 1

	if k < 0:
		k == 0

	n = int(k*100)

	raf = np.zeros(100 , dtype=bool)

	for i in range(0,n):
		raf[i] = True

	return raf[rd.randint(0,len(raf)-1)]

def mutation_ind(ind):
	muta = ind.copy()
	#print(muta)
	anomalia = rd.randint(0,2)
	muta[anomalia] = rd.randint(0,255)
	return muta

def mutation(gen,k): # k: porcentagem de chance de individuo sofrer mutacao
	ret = gen.copy()
	for i in range(0,len(gen)):
		if raffle(k):
			ret[i] = mutation_ind(gen[i])
	return ret

def multiplication(gen,n):
	#print('Gen: '+str(gen))
	if len(gen) < n:
		ret = np.zeros([n,3])
		#print('Ret: '+str(ret))

		for i in range(0,len(gen)):
			ret[i] = gen[i]

		#print('Ret2: '+str(ret))

		for i in range(len(gen),n):
			ret[i] = gen[rd.randint(0,len(gen)-1)]

		#print('Ret3: '+str(ret))
		return ret
	else:
		return gen