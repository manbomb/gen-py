# Gen-py
Some functions of genetic algorithms (I'm learning about it).

* **new_gen(n)**: Create a new random generation with n individuals.
* **fit_fun_ind(ind)**: To calculate an individual's fit value.
* **fit_fun(gen)**: To calculate an generation's (n individuals) fit value.
* **selection(gen, fit_fun, k)**: To select the best individuals, gen is the generation, k is the percentage of individuals that to be select.
* **cross_over(gen)**: to cross the genomes of individuals of the generation. *Example: AAA and BBB -> ABA and BAB*
* **raffle(k)**: a Boolean return function that depends on k percentage chance.
* **mutation_ind(ind)**: to transform (randomly) a single genome of the individual. *Example: AAA -> ACA*
* **mutation(gen)**: to transform a generation.
* **multiplication(gen, n)**: to copy the individuals of gen (randomly) until reaching n individuals.

## Example :

```
import gen_py as gp # import the functions 
import numpy as np # import numpy lib

n = 10 # number of individuals
gen = gp.new_gen(n) # create a new generation

t = 0 # counter of generations

while True:
	print(t) # print the t
	t += 1   # add 1 to t
	gen = gp.selection(gen, gp.fit_fun, 0.2) # select the best two
	gen = gp.cross_over(gen) # cross the two selected
	gen = gp.multiplication(gen, n) # copy them to reach 10 individuals
	gen = gp.mutation(gen, 0.1) # make mutations
	test = gen.copy() # copy gen to calc fit
	fit = gp.fit_fun(test) # calc fit to gen's individuals
 
	if fit.max() > 0.99: # 0.99 is the objective of fit
		break # get out the cicle

print(fit.max()) # print the best fit value
print(gen[np.argmax(fit)]) # print the best individual
```

## Results :

The folder 'results' contains two HTML archives, the first, 'fit.html' shows a chart of the fit values to each generation, the second, 'cor.html' shows the visual evolution of the colors.

![Fit Chart](/results/fit_chart.png)

## Problems :

The cross function should increase the quantity of individuals without lose the original individuals, the parent individuals. The mutation do not should be randomly, because, some times the mutationed individual is too much different. Decreasing the result of a generation. These two problems mentioned can be seen in the fit graph. The evolution is not clear.
