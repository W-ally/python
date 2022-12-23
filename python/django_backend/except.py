'''This file have the purpose of ...'''

# Jerarquía de excepciones. https://dotnettutorials.net/wp-content/uploads/2020/07/word-image-181.png
# try
# except
# else
# finally
# raise

try:
    print(1/0)
except ZeroDivisionError:
    print('No se puede dividir entre cero.')
else:
    print('No se ha generado una excepción.')
finally:
    print('Se ejecuta siempre.')

