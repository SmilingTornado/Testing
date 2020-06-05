# author:
# assignment:
# description:

import input_parsing as ip
from random import randint
from time import sleep


def game(difficulty):
    wmin = (difficulty + 1) // 2
    wmax = 2 * wmin
    round_length = difficulty + 2
    score = 0
    while True:
        nums = []
        inputs = []
        print('- Level 1 -')
        for i in range(round_length):
            nums.append(randint(10 ** (wmin - 1), (10 ** wmax) - 1))
            print(nums[i])
        print('The round starts in 10 seconds!')
        sleep(10)
        print('10 seconds passed')
        print('\n' * 40)
        correct = True
        inputs.append(ip.int_input('Enter the first number: '))
        if nums[0] != inputs[0]:
            print('Incorrect Number!')
            correct = False
        else:
            score += difficulty * 10
        for i in range(1, round_length):
            inputs.append(ip.int_input('Enter the next number: '))
            if nums[i] != inputs[i]:
                print('Incorrect Number!')
                correct = False
            else:
                score += difficulty * 10
        if correct:
            print('Congratulations. You won the round! Your Score: %d' % score)
            option = ip.give_options('Enter 1 to play another round, 2 to see the principal menu again, or 3 to exit: ',
                                     ['1', '2', '3'], 'Invalid Option. ')
            if option == '1':
                continue
            elif option == '2':
                break
            else:
                quit()

        else:
            print('Game Over! Your points: %d' % score)
            option = ip.give_options(
                'Enter 1 to return to the main menu or 2 to exit: ',
                ['1', '2', '3'], 'Invalid Option. ')
            if option == '1':
                break
            else:
                quit()
    return score


difficulty = 1
highest_score = 0
while True:
    score_spacing = " " * (7 - len(str(highest_score)))  # Calculating padding for score line
    option = ip.give_options("============ MEMOGAME ===========\n"
                             "|                               |\n"
                             "| 1. Choose level of difficulty |\n"
                             "| 2. Start Game                 |\n"
                             "| 3. Exit the Game              |\n"
                             "|                               |\n"
                             "| Current Difficulty %d/5        |\n"
                             "| Highest score reached: %d%s|\n"
                             "|                               |\n"
                             "---------------------------------\n" % (difficulty, highest_score, score_spacing),
                             ['1', '2', '3'])
    if option == '1':
        difficulty = ip.ranged_int_input(1, 5, 'Enter your desired difficulty level')
    elif option == '2':
        score_achieved = game(difficulty)
        if highest_score < score_achieved:
            highest_score = score_achieved
    elif option == '3':
        break
