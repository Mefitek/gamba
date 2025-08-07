
import random



# =================================
# =======     CONSTANTS     =======
# =================================
SYMBOLS = [0,1,2,3,4,5,6,7,8] # symbols 🍉, 💲, 🍒, 🟣, ⭐, 🔔, 🍇, 🍊, 🧊
USE_EMOJIS = True
replacements = {0:"🍉", 1:"💲", 2:"🍒", 3:"🟣", 4:"⭐", 5:"🔔", 6:"🍇", 7:"🍊", 8:"🧊"}
replacer = replacements.get # For faster gets.
CYLS = 3
CYL_SLOTS = 3


class Pokie:

    def __init__(self, cylinders : int, cyl_slots : int):
        self.cylinders = cylinders
        self.cyl_slots = cyl_slots
        self.pokie = [[-1]*cyl_slots]*cylinders
        return

    def print_pokie(self):
        if not USE_EMOJIS:
            for row in self.pokie:
                print(row)
        else:
            for row in self.pokie:
                print([replacer(n, n) for n in row])
        return
    
    def spin(self, symbols : list):
        for c in range(self.cylinders):
                self.pokie[c] = random.choices(symbols, k=self.cyl_slots)
        self.pokie = [list(row) for row in zip(*self.pokie)] # transpose (needed for checking the winning lines later)
        return



p = Pokie(CYLS, CYL_SLOTS)
p.spin(SYMBOLS.copy())
p.print_pokie()

