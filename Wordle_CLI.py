import random
import requests
import re
from colorama import Fore, init

init(autoreset=True)  # Automatically reset to default color after each print

# Word List URL
url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
# url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(url)
words = response.text.splitlines()

five_letter = [word for word in words if len(word) == 5]
random_word = random.choice(five_letter).upper()

attempts = 6
results = []

def check_word(input, rand):
    result = ""
    for i in range(5):
        if input[i] == rand[i]:
            result += Fore.GREEN + input[i]  # Green for correct letter and position
        elif input[i] in rand:
            result += Fore.YELLOW + input[i]  # Yellow for correct letter but wrong position
        else:
            result += Fore.LIGHTBLACK_EX + input[i]  # Gray (or light black) for incorrect letter
    return result

def check_eng(input):
    return bool(re.match("^[A-Z]{5}$", input))

for _ in range(attempts):
    while True:
        user_input = input("Enter a 5-letter word (Attempts Left: {}): ".format(attempts)).upper()
        
        if user_input == "SHOWTHEANSWER":
            print("The answer is {}.".format(random_word))
            attempts += 1
            continue
        if not check_eng(user_input):
            print("Please enter a 5-letter English word.")
            continue
        elif user_input.lower() not in five_letter:
            print("The word you entered is not in the dictionary.")
            continue
        else:
            break
    
    attempts -= 1
    
    if user_input == random_word:
        print("You guessed correctly!")
        break
    else:
        if attempts > 0:
            feedback = check_word(user_input, random_word)
            print("Incorrect! Result: {}".format(feedback))
        else:
            feedback = check_word(user_input, random_word)
            print("Incorrect! Result: {}".format(feedback))
            print("You guessed incorrectly! The word was {}.".format(random_word))
