import re
with open('input.txt') as f:
    game_input = f.readlines()

numeric_entries, dots, syms = [],[],[]
for line in game_input:
    nums = [s.isdigit() for s in line]
    dot = [s == '.' for s in line]
    sym = [-(a+b)+1 for a,b in zip(nums,dot)]
    numeric_entries.append(nums)
    dots.append(dot)
    syms.append(sym)
indices = [[i for i,val in enumerate(sym_list) if val == 1] for sym_list in syms]

# Find the part numbers. Part numbers are adjecent (also diagonally) to a symbol.
# The entries where syms = 1 represent the symbols. Now we only have to find the adjecent numbers.
# Steps to take:
# - check the (max) 8 values around a symbol for being a number. If on left: move left until not number anymore : add all 
    
# other option: start from the numbers -> re.finditer('\d+',line) and use .span() to find start and end, and int(.group()) to get out the interger for summing after checking left and right around for symbols, in the symbol lattice.

coordinates = []
for y,lst in enumerate(indices):
    coordinates+= [(y,x) for x in lst]