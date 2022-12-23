'''This file have the purpose of explain how conditionals works'''

# Equals
# Not Equals
# Less than
# Less than or equal to
# Greater than
# Greater than or equal to
# if
# elif
# else

def current_speed (distance, time):
    speed = distance / time
    if speed < 10:
        return 'You are going to slow'
    elif speed > 80:
        return 'You are going too fast'
    else:
        return 'You are going OK'

print(current_speed(100, 5))