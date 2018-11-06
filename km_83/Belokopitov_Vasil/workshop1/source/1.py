from km_83.Belokopitov_Vasil.workshop1.functions import sqrFunction
from km_83.Belokopitov_Vasil.workshop1.functions import floatFunction
x = floatFunction(input("Введіть х: "))
if x<=3:
    res = sqrFunction(1,-3,9,x)
else:
    res = 1/(x**2 + 6)
print(res)