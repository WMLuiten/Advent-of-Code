import re

reg_exp = '(\d+) (\w+)'
with open('input.txt') as f:
    game_input = f.readlines()

maximums = {'red':12, 'green':13, 'blue':14}
result = 0
for gamenr, line in enumerate(game_input, start =1):
    validGame = True
    cubes = re.findall(reg_exp,line)
    for value, colour in cubes:
        if int(value) > maximums[colour]: 
            validGame = False
            break
    if validGame:
        result += gamenr
print(result)