################################
# Pema Tashi
# 1st year ECE
# 02230101
################################
# REFERENCES
# https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
# https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1204/handouts/py-file.html
# https://www.youtube.com/watch?v=oAFkPMbwRVY
################################
# SOLUTION
# Your Solution Score:
# 50055
################################

# Reading the input text file.

def read_input(given_file):
    turns = []   # It stores the result extracted from the file stored as tuple.
    f = open(given_file, 'r')      
    line = f.readline()    # Reads a line from the file.
    # The code iterates until there is no more value in the line.
    while line: #Since line holds the value, it is true.Therefore block of code below is excuted.
        strip_line = line.strip()  #Get rid of any empty spaces at the beginning or end of the string.
        shape, result = strip_line.split()  # makes strings list.
        turns.append((shape, result))
        line = f.readline()   # Reads a new line.
    f.close()
    return turns   

# Calculating the scores.

def calculate_score(rounds):

# Using for loops to iterate many times.
# And using nested if else conditional statements for the game to get scores as per the shape and the result(win/lose/draw) of the game.

    final_score = 0   # keeping the final score as 0 for now to add later on.
    for shape, result in rounds:
        if shape == "A":   # the shape is rock
            if result == "X":   # the result is to lose. I need to show scissor.
                final_score += 3   # 3+0 = 3. Therefore score 3 is added
            elif result == "Y":   # the result is draw. I need to show rock
                final_score += 4   # 1+3 = 4. Therefore score 4 is added
            else:   # the result is win. I need to show paper
                final_score += 8   # 2+6 = 8. Therefore score 8 is added
        elif shape == "B":   # the shape is paper
            if result == "X":   # the result is to lose. I need to show rock
                final_score += 1   # 1+0 = 1. Therefore score 1 is added
            elif result == "Y":   # the result is draw. I need to show paper
                final_score += 5   # 2+3 = 5. Therefore score 5 is added
            else:   # the result is to win. I need to show scissor
                final_score += 9   # 3+6 = 9. Therefore score 9 is added
        else:   # the shape is scissor
            if result == "X":   # the result is to lose. I need to show paper
                final_score += 2   # 2+0 = 2. Therefore score 2 is added
            elif result == "Y":   # the result is draw. I need to show scissor
                final_score += 6   # 3+3 = 6. Therefore score 6 is added
            else:   # the result is to win. I need to show rock
                final_score += 7   # 1+6 = 7. Therefore score 7 is added
    return final_score

given_file = "input_1_cap1.txt"  #replacing the file with input_1_cap1.txt
rounds = read_input(given_file)
print("the total score is:", calculate_score(rounds))
