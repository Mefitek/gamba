
import random

# TODO: Documentation

 # ----- CONSTANTS -----
SYMBOLS = [0,1,2,3,4,5,6,7,8] # symbols 🍒, 🟣, 🍇, 🍊, 💲, 🔔, 🍉, ⭐, 🧊
SYMBOLS = [0,0,0,0,0,0,0,0,0,
           1,1,1,1,1,1,
           2,2,2,2,
           3,3,3,3,
           4,4,4,4,
           5,5,5,
           6,6,
           7,7,
           8]
WILD_SYMBOL = 8 # 🧊
USE_EMOJIS = True
replacements = {0:"🍒", 1:"🟣", 2:"🍇", 3:"🍊", 4:"💲", 5:"🔔", 6:"🍉", 7:"⭐", 8:"🧊"}
replacer = replacements.get # For faster gets.
scores = {0:2, 1:2, 2:5, 3:5, 4:10, 5:10, 6:20, 7:50, 8:0}
scores_replacer = scores.get # For faster gets.
CYLS = 3
CYL_SLOTS = 3
BONUS_GAME_MIN = 2000
BONUS_GAME_MAX = 4330


class Pokie:

    def __init__(self, cylinders : int, cyl_slots : int):
        self.cylinders = cylinders
        self.cyl_slots = cyl_slots
        self.pokie = [[-1]*cyl_slots]*cylinders
        self.last_score = 0
        return

    def set_pokie(self, new_pokie: list):
        self.pokie = new_pokie

    def print_pokie(self):
        if not USE_EMOJIS:
            for row in self.pokie:
                print(row)
        else:
            for row in self.pokie:
                print([replacer(n, n) for n in row])
        print()
        return
    
    def spin(self, symbols : list):
        for c in range(self.cylinders):
                self.pokie[c] = random.sample(symbols, k=self.cyl_slots)
        self.pokie = [list(row) for row in zip(*self.pokie)] # transpose (needed for checking the winning lines later)
        return
    
    def spin2(self, symbols : list):
        symbols += symbols # primitive overflow protection
        for c in range(self.cylinders):
            offset = random.randint(0,self.cyl_slots)
            self.pokie[c] = symbols[offset:offset+self.cyl_slots]
        self.pokie = [list(row) for row in zip(*self.pokie)] # transpose (needed for checking the winning lines later)
        return

    def spin3(self, symbols : list):
        for c in range(self.cylinders):
                self.pokie[c] = random.choices(symbols, k=self.cyl_slots)
        self.pokie = [list(row) for row in zip(*self.pokie)] # transpose (needed for checking the winning lines later)
        return
    
    def count_score(self):
        lines = []
        # ----- ROWS -----
        for row in self.pokie:
            lines.append(row)
        # ------ DIAGONALS ------
        if self.cylinders == self.cyl_slots: # otherwise there are no diagonals
            d1, d2 = get_diagonals(self.pokie)
            lines.append(d1)
            lines.append(d2)

        # ------ COUNT SCORE  ------
        total_score = 0
        for line in lines:
            score = 0
            symbol_count = len(set(line)) # convert row to set, then get length
            if symbol_count == 1:
                if WILD_SYMBOL in line: # BONUS GAME
                    score = random.randint(BONUS_GAME_MIN, BONUS_GAME_MAX)
                    #print(f"{emoji(line)}\tBONUS GAME score: {score}")
                else: # COUNT SCORE
                    score = [scores_replacer(n, n) for n in line][0]
                    #print(f"{emoji(line)}\tscore: {score}")
            elif (symbol_count == 2) and (WILD_SYMBOL in line) : # WILD SYMBOL MULTIPLIER
                mult = pow(2, line.count(WILD_SYMBOL))
                score = mult*max([scores_replacer(n, n) for n in line])
                #print(f"{emoji(line)}\tscore: {score}")
            total_score += score
        #print(f"Total score = {total_score}\n")
        self.last_score = total_score

'''
Get both diagonals of an array
'''
def get_diagonals(arr):
    diag1 = []
    diag2 = []
    rows = len(arr)
    cols = len(arr[0])
    for r in range(rows):
        for c in range(cols):
            if r==c:
                diag1.append(arr[r][c])
            if r+c == rows-1:
                diag2.append(arr[r][c])
    diag2 = diag2[::-1] # mirror to be correct
    return diag1, diag2

def emoji(row):
    return [replacer(n, n) for n in row]


'''
Simulate N games
'''
def sim(spins:int, cost:int):
    p = Pokie(CYLS, CYL_SLOTS)
    score = 0
    for game in range(spins):
        #p.spin(SYMBOLS.copy())
        p.spin(SYMBOLS.copy())
        p.count_score()
        score += p.last_score
    print(f"\nSpins:\t{spins}\nScore:\t{score}\nRTP:\t{round(score/(spins*cost)*100,2)} %")
    return score

'''
p = Pokie(CYLS, CYL_SLOTS)
p.spin(SYMBOLS.copy())
p.print_pokie()
p.count_score()
'''
spins = 10000000
cost = 2
sim(spins, cost)

