def lagrange_interpolation(x_values, y_values):
    n = len(x_values)
    coefficients = []
    
    for i in range(n):
        numerator = [] # массив для хранения числителя дроби в формуле
        denominator = 1 # начальный знаменатель дроби в формуле
        
        for j in range(n):
            if i != j:
                numerator.append('(x - {})'.format(x_values[j])) # добавляем в массив часть числителя формулы
                denominator *= (x_values[i] - x_values[j]) # умножаем знаменательн на разность xi и xj
        
        coefficient = '*'.join(numerator) + ' / ' + str(denominator) # обьединяем все элементы массива числителей numerator и делим на знаменатель denominator
        coefficients.append('(' + str(y_values[i]) + ')*' + coefficient) # добавляем полученную строку в результирующий массив коэффициентов
    
    return coefficients


#x = [1, 2, 3, 4, 5, 6, 7, 8] #для 7го
#y = [4, 1, 3, 2, 6, 9, 200, 30] 

x = [1, 2, 3, 4, 5, 6] #для 5го
y = [4, 1, 3, 2, 6, 9]

coefficients = lagrange_interpolation(x, y)
formula = ' + '.join(coefficients) #обьединяем все коэффициенты и получаем формулу
print(formula)