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

    guess = guess_entry.get().lower()

    if not is_valid_guess(guess, guesses):
        status_label.config(text="invalid guess")
        return

    if attempts >= max_attempts:
        return

    colors = evaluate_guess(guess, secret_word)

    for col in range(5):
        grid_labels[attempts][col].config(
            text=guess[col].upper(),
            bg=colors[col],
            fg="white"
        )

    if guess == secret_word:
        status_label.config(text="you win!")
        guess_entry.config(state="disabled")
        return

    attempts += 1

    if attempts == max_attempts:
        status_label.config(text=f"game over. word was {secret_word}")
        guess_entry.config(state="disabled")

    guess_entry.delete(0, tk.END)


guesses_dictionary = "guesses.txt"
answers_dictionary = "answers.txt"

guesses = load_dictionary(guesses_dictionary)
answers = load_dictionary(answers_dictionary)

secret_word = random.choice(answers).lower()

attempts = 0
max_attempts = 6


root = tk.Tk()
root.title("wordle")
root.geometry("420x500")


main_frame = tk.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor="center")


title_label = tk.Label(
    main_frame,
    text="wordle",
    font=("Arial", 26, "bold")
)

title_label.grid(row=0, column=0, columnspan=5, pady=10)


grid_labels = []

for row in range(6):

    label_row = []

    for col in range(5):

        cell = tk.Label(
            main_frame,
            text="",
            width=4,
            height=2,
            font=("Arial", 22),
            relief="solid"
        )

        cell.grid(row=row + 1, column=col, padx=5, pady=5)

        label_row.append(cell)

    grid_labels.append(label_row)


guess_entry = tk.Entry(
    main_frame,
    font=("Arial", 16),
    justify="center"
)

guess_entry.grid(row=8, column=0, columnspan=3, pady=20)


submit_button = tk.Button(
    main_frame,
    text="submit",
    command=submit_guess
)

submit_button.grid(row=8, column=3, columnspan=2)


status_label = tk.Label(
    main_frame,
    text=""
)

status_label.grid(row=9, column=0, columnspan=5)


root.mainloop()