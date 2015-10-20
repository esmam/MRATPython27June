from eelbrain import *
from eelbrain import Factor
import numpy as np

np.random.seed(2)

y = np.empty(21)
y[:14] = np.random.normal(0, 1, 14)
y[14:] = np.random.normal(1.5, 1, 7)

Y = Var(y, 'Y')
A = Factor('abc', 'A', repeat=7)

d = Dataset((Y, A))
f =  table.frequencies(A)
c = test.anova(Y, A)
v =  test.pairwise(Y, A, corr='Hochberg')

t = test.pairwise(Y, A, corr='Hochberg')
z =  t.get_tex()

plot.Boxplot(Y, A, title="My Boxplot", ylabel="value", corr='Hochberg')