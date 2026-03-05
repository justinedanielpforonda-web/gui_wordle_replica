import random
import tkinter as tk

def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words


def is_valid_guess(guess, guesses):
    return len(guess) == 5 and guess in guesses


def evaluate_guess(guess, word):
    result = ""

    for i in range(5):
        if guess[i] == word[i]:
            result += guess[i]
        else:
            if guess[i] in word:
                result += guess[i]
            else:
                result += guess[i]

    return result


def submit_guess():
    guess = entry.get().lower()

    if not is_valid_guess(guess, guesses):
        status_label.config(text="Invalid guess.")
        return

    feedback = evaluate_guess(guess, secret_word)
    result_label.config(text=feedback)


guesses_dictionary = "guesses.txt"
answers_dictionary = "answers.txt"

guesses = load_dictionary(guesses_dictionary)
answers = load_dictionary(answers_dictionary)

secret_word = random.choice(answers).lower()

# GUI
root = tk.Tk()
root.title("Wordle")

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_guess)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()