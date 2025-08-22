from constants import HIGH_SCORE_FILE
from constants import CURRENT_SCORE_FILE

# returns the number written in the HIGH_SCORE_FILE
def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            score = int(file.read())
            return score
    except (FileNotFoundError, ValueError):
        return 0

# returns the number written in the CURRENT_SCORE_FILE
def load_current_score():
    try:
        with open(CURRENT_SCORE_FILE, "r") as file:
            score = int(file.read())
            return score
    except (FileNotFoundError, ValueError):
        return 0

# check if new_score is higher than value stored in HIGH_SCORE_FILE, write in new value if new_score is higher
def save_high_score(new_score):
    current_high_score = load_high_score()
    if new_score > current_high_score:
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(new_score))

# write player_score value to Current_score_file
def save_current_score(player_score):
    with open(CURRENT_SCORE_FILE, "w") as file:
        file.write(str(player_score))