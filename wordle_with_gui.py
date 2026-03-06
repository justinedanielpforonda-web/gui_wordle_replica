import random
import tkinter as tk



def load_dictionary(file_path):
    with open(file_path) as file:
        words = [line.strip() for line in file]
    return words



def is_valid_guess(guess, guesses):
    return len(guess) == 5 and guess in guesses



def evaluate_guess(guess, secret_word):
    colors = []

    for i in range(5):
        if guess[i] == secret_word[i]:
            colors.append("#6aaa64")  # green
        elif guess[i] in secret_word:
            colors.append("#c9b458")  # yellow
        else:
            colors.append("#787c7e")  # gray

    return colors



def submit_guess(event=None):
    global attempts

    guess = guess_entry.get().lower()

    if not is_valid_guess(guess, guesses):
        status_label.config(text="Invalid guess.")
        return

    if attempts >= max_attempts:
        return

    colors = evaluate_guess(guess, secret_word)

    for col in range(5):
        grid_labels[attempts][col].config(
            text=guess[col].upper(),
            bg=colors[col]
        )

    if guess == secret_word:
        status_label.config(text="🎉 You guessed the word!")
        guess_entry.config(state="disabled")
        return

    attempts += 1

    if attempts == max_attempts:
        status_label.config(
            text=f"Game Over! Word was {secret_word.upper()}"
        )
        guess_entry.config(state="disabled")

    guess_entry.delete(0, tk.END)



def restart_game():
    global secret_word, attempts

    secret_word = random.choice(answers).lower()
    attempts = 0

    for row in grid_labels:
        for cell in row:
            cell.config(text="", bg="black")

    guess_entry.config(state="normal")
    guess_entry.delete(0, tk.END)
    status_label.config(text="")



def keyboard_press(letter):
    current = guess_entry.get()

    if len(current) < 5:
        guess_entry.insert(tk.END, letter)



guesses = load_dictionary("guesses.txt")
answers = load_dictionary("answers.txt")

secret_word = random.choice(answers).lower()

attempts = 0
max_attempts = 6



root = tk.Tk()
root.title("Wordle GUI")
root.geometry("500x700")
root.configure(bg="black")


main_frame = tk.Frame(root, bg="black")
main_frame.place(relx=0.5, rely=0.5, anchor="center")


title_label = tk.Label(
    main_frame,
    text="WORDLE",
    font=("Arial", 30, "bold"),
    fg="white",
    bg="black"
)

title_label.grid(row=0, column=0, columnspan=5, pady=15)



grid_labels = []

for row in range(6):

    row_boxes = []

    for col in range(5):

        box = tk.Label(
            main_frame,
            text="",
            width=4,
            height=2,
            font=("Arial", 26, "bold"),
            fg="white",
            bg="black",
            relief="solid",
            bd=2
        )

        box.grid(row=row + 1, column=col, padx=5, pady=5)

        row_boxes.append(box)

    grid_labels.append(row_boxes)



guess_entry = tk.Entry(
    main_frame,
    font=("Arial", 16),
    justify="center"
)

guess_entry.grid(row=8, column=0, columnspan=3, pady=20)

guess_entry.bind("<Return>", submit_guess)


submit_button = tk.Button(
    main_frame,
    text="Submit",
    command=submit_guess
)

submit_button.grid(row=8, column=3, columnspan=2)



status_label = tk.Label(
    main_frame,
    text="",
    fg="white",
    bg="black",
    font=("Arial", 12)
)

status_label.grid(row=9, column=0, columnspan=5)



restart_button = tk.Button(
    main_frame,
    text="Restart",
    command=restart_game
)

restart_button.grid(row=10, column=0, columnspan=5, pady=10)



keyboard_frame = tk.Frame(root, bg="black")
keyboard_frame.pack(side="bottom", pady=20)

keyboard_rows = [
    "QWERTYUIOP",
    "ASDFGHJKL",
    "ZXCVBNM"
]

for r, row in enumerate(keyboard_rows):

    frame = tk.Frame(keyboard_frame, bg="black")
    frame.pack()

    for letter in row:

        btn = tk.Button(
            frame,
            text=letter,
            width=4,
            command=lambda l=letter: keyboard_press(l.lower())
        )

        btn.pack(side="left", padx=2, pady=2)


root.mainloop()