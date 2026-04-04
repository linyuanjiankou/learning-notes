import random
def randominteger(min_val, max_val):
    return random.randint(min_val, max_val)

score = 0
for game_round in range(1, 4):
    number = randominteger(1, 5)

    if number == 3:
        score = 0
    elif number == 2 or number == 4:
        score -=5
    else:
        score +=10

print(f"final score: {score}")