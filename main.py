import random
import tkinter as tk

# Define a function to check the user's guess
def check_guess():
    guess = int(guess_entry.get())
    if guess == number:
        result_label.config(text="You guessed it! The number was " + str(number))
    elif guess < number:
        result_label.config(text="Too low! Guess again.")
    else:
        result_label.config(text="Too high! Guess again.")

# Create a new random number for the user to guess
number = random.randint(1, 100)

# Create a new Tkinter window
root = tk.Tk()
root.title("Number Guessing Game")

# Create a label and input field for the user's guess
guess_label = tk.Label(root, text="Guess a number between 1 and 100:")
guess_label.grid(row=0, column=0)

guess_entry = tk.Entry(root)
guess_entry.grid(row=0, column=1)

# Create a button to check the user's guess
guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.grid(row=1, column=0, columnspan=2)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
