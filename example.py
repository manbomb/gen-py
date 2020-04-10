import gen_py as gp
import numpy as np

n = 10
gen = gp.new_gen(n)

t = 0

file = open('log.js', 'a')
file2 = open('fit_log.js', 'a')

while True:
	print(t)
	t += 1
	gen = gp.selection(gen, gp.fit_fun, 0.2)
	gen = gp.cross_over(gen)
	gen = gp.multiplication(gen, n)
	gen = gp.mutation(gen, 0.1)
	test = gen.copy()
	fit = gp.fit_fun(test)

	x = gen[np.argmax(fit)].astype('str').tolist()
	file.write('\'rgb('+','.join(x)+")',\n")

	file2.write(str(fit.max())+",\n")

	if fit.max() > 0.99:
		break

print(fit.max())
print(gen[np.argmax(fit)])

file.close()
file2.close()