import re

def part1(inputlist):
    result = 0
    for l in elf_enc:
        digits = re.findall("\d",l)
        if len(digits) > 0:
            result += int(digits[0] + digits[-1])
    return result

def replace_words(line):
    replacements = {'one':'o1e','two':'t2o','three':'t3e','four':'4','five':'5e','six':'6','seven':'7n','eight':'e8t','nine':'n9e'}
    line = line.lower()
    for k, v in replacements.items():
        line = line.replace(k,v)
    return line

def part2(inputlist):
    for idx,line in enumerate(inputlist):
        inputlist[idx] = replace_words(line)
    return part1(inputlist)

if __name__ == '__main__':
    with open('input.txt') as f:
        elf_enc = f.readlines()
    
    print( 'part 1 result = ' + str(part1(elf_enc)))
    print( 'part 2 result = ' + str(part2(elf_enc)))
