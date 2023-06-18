import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff

### Ищем полином

# Определение переменных и коэффициентов
t = sp.Symbol('t')
a, b, c, d, e, f = sp.symbols('a b c d e f')
T = 5
Te= T

# Определение пятимерной полиномиальной функции временного масштабирования
polynomial = a * t**5 + b * t**4 + c * t**3 + d * t**2 + e * t + f

# Определение ограничений (constraints)
constraints = [
    sp.Eq(polynomial.subs(t, 0), 0), #задаем что a * 0**5 + b * 0**4 + c * 0**3 + d * 0**2 + e * 0 + f =0, т.е. S(0) = 0
    sp.Eq(sp.diff(polynomial, t).subs(t, 0), 0), #задаем что 5a * 0**4 + 4b * 0**3 + 3c * 0**2 + 2d * 0**1 + e = 0, т.е. S'(0) = 0
    sp.Eq(sp.diff(polynomial, t, 2).subs(t, 0), 0), #задаем что 20a * 0**3 + 12b * 0**2 + 6c * 0**1 + 2d= 0, т.е. S''(0) = 0
    sp.Eq(polynomial.subs(t, T), 1), #задаем что a * T**5 + b * T**4 + c * T**3 + d * T**2 + e * T + f =1, т.е. S(T) = 1
    sp.Eq(sp.diff(polynomial, t).subs(t, T), 0), #задаем что 5a * T**4 + 4b * T**3 + 3c * T**2 + 2d * T**1 + e = 0, т.е. S'(T) = 0
    sp.Eq(sp.diff(polynomial, t, 2).subs(t, T), 0) #задаем что 20a * T**3 + 12b * T**2 + 6c * T**1 + 2d= 0, т.е. S''(T) = 0
]

# Решение системы уравнений
solution = sp.solve(constraints, (a, b, c, d, e, f))
# Подстановка решений в полиномиальную функцию
polynomial = polynomial.subs(solution)
# Вывод полиномиальной функции
print(polynomial)
print(solution)

Answer = solution[a] * t**5 + solution[b] * t**4 + solution[c] * t**3 + solution[d] * t**2 + solution[e] * t + solution[f]

### Построим график траектории
t = np.linspace(0, Te, 100)
S = solution[a] * t**5 + solution[b] * t**4 + solution[c] * t**3 + solution[d] * t**2 + solution[e] * t + solution[f]
plt.plot(t, S)
plt.xlabel('t')
plt.ylabel('S')
plt.title('График траектории')
plt.grid(True)
plt.show()


### Построим график скорости
t = np.linspace(0, Te, 100)
S = (5*solution[a] * t**4) + (4*solution[b] * t**3) + (3*solution[c] * t**2) + (2*solution[d] * t) + solution[e] 
plt.plot(t, S)
plt.xlabel('t')
plt.ylabel('S')
plt.title('График скорости')
plt.grid(True)
plt.show()

### Построим график ускорения
t = np.linspace(0, Te, 100)
S = 20*solution[a] * t**3 + 12*solution[b] * t**2 + 6*solution[c] * t + 2*solution[d] 
plt.plot(t, S)
plt.xlabel('t')
plt.ylabel('S')
plt.title('График ускорения')
plt.grid(True)
plt.show()


### Построим график 3й производной
t = np.linspace(0, Te, 100)
S = 60*solution[a] * t**2 + 24*solution[b] * t + 6*solution[c] 
plt.plot(t, S)
plt.xlabel('t')
plt.ylabel('S')
plt.title('График 3й производной')
plt.grid(True)
plt.show()