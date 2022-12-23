'''This file have the purpose of ...'''

# while -  break
# while - continue
# while - else
# for - recorriendo cadenas de texto
# for - break
# for - continue
# for - range
# for - else

increment = 0
while increment < 10:
    increment += 1
    if increment == 5:
        continue
    print(increment)
    if increment == 8:
        break

x  = range(10)
for i in x:
    print(i)
    if i == 5:
        i = 8
