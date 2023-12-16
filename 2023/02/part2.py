import re

reg_exp = '(\d+) (\w+)'
with open('input.txt') as f:
    game_input = f.readlines()

res = 0
for line in game_input:
    cubes = re.findall(reg_exp,line)
    pwr = 1
    for col in ['blue','green','red']:
        pwr *= max([int(value) for value, colour in cubes if colour == col])
    res += pwr

print(res)