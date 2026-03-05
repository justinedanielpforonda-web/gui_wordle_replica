import random
import tkinter as tk

def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words


def is_valid_guess(guess, guesses):
    return len(guess) == 5 and guess in guesses


def evaluate_guess(guess, word):
    colors = []

    for i in range(5):
        if guess[i] == word[i]:
            colors.append("green")
        elif guess[i] in word:
            colors.append("yellow")
        else:
            colors.append("gray")

    return colors


def submit_guess():
    global attempts

    guess = entry.get().lower()

    if not is_valid_guess(guess, guesses):
        status_label.config(text="Invalid guess")
        return

    colors = evaluate_guess(guess, secret_word)

    for i in range(5):
        grid_labels[attempts][i].config(
            text=guess[i].upper(),
            bg=colors[i]
        )

    attempts += 1

    entry.delete(0, tk.END)


guesses_dictionary = "guesses.txt"
answers_dictionary = "answers.txt"

guesses = load_dictionary(guesses_dictionary)
answers = load_dictionary(answers_dictionary)

secret_word = random.choice(answers).lower()

attempts = 0

root = tk.Tk()
root.title("Wordle")

grid_labels = []

for r in range(6):
    row = []
    for c in range(5):

        lbl = tk.Label(
            root,
            text="",
            width=4,
            height=2,
            relief="solid"
        )

        lbl.grid(row=r, column=c)

        row.append(lbl)

    grid_labels.append(row)

entry = tk.Entry(root)
entry.grid(row=7, column=0, columnspan=3)

submit_button = tk.Button(root, text="Submit", command=submit_guess)
submit_button.grid(row=7, column=3, columnspan=2)

status_label = tk.Label(root, text="")
status_label.grid(row=8, column=0, columnspan=5)

root.mainloop()