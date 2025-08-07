
import random

# TODO: rework so that Pokie is a class

SYMBOLS = [0,1,2,3,4,5,6,7,8] # symbols 🍉, 💲, 🍒, 🟣, ⭐, 🔔, 🍇, 🍊, 🧊
USE_EMOJIS = False
replacements = {0:"🍉", 1:"💲", 2:"🍒", 3:"🟣", 4:"⭐", 5:"🔔", 6:"🍇", 7:"🍊", 8:"🧊"}
replacer = replacements.get # For faster gets.

'''
TODO: Docu
'''
def print_pokie(pokie):
    if not USE_EMOJIS:
        for row in pokie:
            print(row)
    else:
        for row in pokie:
            print([replacer(n, n) for n in row])
        

'''
TODO: Docu
    shuffle True assumes that the symbols revolve around the cylinder in random order each spin
    shuffle False assumes that the symbols revolve around all cylinders in the same order (0 to 8)
    cylinders - how many columns (cylinders) of slot machine
    cyl_slots = how many rows (symbols on cylinder) visible after spin
'''
def spin(symbols : list, cylinders : int, cyl_slots : int):
    pokie = [[-1]*cylinders]*cyl_slots
    for c in range(cylinders):
            pokie[c] = random.choices(symbols, k=cyl_slots)
    pokie = [list(row) for row in zip(*pokie)] # transpose (needed for checking the winning lines later)
    return pokie



pokie = spin(SYMBOLS.copy(), 3, 3)
print_pokie(pokie)
