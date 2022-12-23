'''This file have the purpose of ...'''

# Asignacion de variables
country = "Mexico"
city = "Mexico City"
country_code = "52"

# Casting
country_code = int(country_code)

# Case Sensitive
var = 0
vAr = 0
# lower_snake_case https://peps.python.org/pep-0008/
# Varios valores, varias variables
var_1, var_2, var_3 = 1, 2, 3
# Un valor, varias variables
var1 = var_2 = var_3 = 1
# Valores de collections  a varias variables
var_1, var_2, var_3 = [1, 2, 3]
# Variables globales

def call():
    global var
    var = 1

call()
print(var)