import random
import requests
import tkinter as tk
import tkinter.messagebox as messagebox
import re

# Word List URL
url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
# url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(url)
words = response.text.splitlines()

five_letter = [word for word in words if len(word) == 5]
random_word = random.choice(five_letter).upper()

attempts = 0

def check_word(input, rand):
    result = []
    for i in range(5):
        if input[i] == rand[i]:
            result.append("green")
        elif input[i] in rand:
            result.append("yellow")
        else:
            result.append("gray")
    return result

def check_eng(input):
    return bool(re.match("^[A-Z]{5}$", input))

def display_result(colors, word):
    global attempts
    for i in range(5):
        color = colors[i]
        letter = word[i]
        lbls[attempts][i].config(bg=color, text=letter)

def on_enter(event=None):
    global attempts
    user_input = word_entry.get().upper()
    word_entry.delete(0, tk.END)

    if not check_eng(user_input):
        messagebox.showerror("Error", "Please enter a 5-letter English word.")
        return

    if user_input.lower() not in five_letter:
        messagebox.showerror("Error", "This word is not in the dictionary.")
        return

    colors = check_word(user_input, random_word)
    display_result(colors, user_input)
    attempts += 1

    if user_input == random_word:
        messagebox.showinfo("Congratulations!", "You guessed correctly!")
        return
    elif attempts >= 6:
        messagebox.showinfo("Sorry!", "You guessed incorrectly! The word was {}.".format(random_word))
        return

root = tk.Tk()
root.title("Wordle Game")
root.configure(bg="white")

word_entry = tk.Entry(root, font=("Arial", 20), justify="center", width=10)
word_entry.pack(pady=20)
word_entry.bind("<Return>", on_enter)

lbls = []

for _ in range(6):
    frame = tk.Frame(root, bg="white")
    frame.pack(pady=5)
    row = []
    for i in range(5):
        lbl = tk.Label(frame, font=("Arial", 20), width=2, height=1, bg="white", relief="solid", borderwidth=1)
        lbl.pack(side="left", padx=5)
        row.append(lbl)
    lbls.append(row)

root.mainloop()
