import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
# from quiz_data import quiz_data
quiz_data = [
    # Maths Questions
    {
        "category": "Maths",
        "question": "Which of the following is the solution to the equation 0.5x^2 + 3x -5=0 ?",
        "choices": ["x = -5", "x = 5", "x = 4", "x = -4"],
        "answer": "x = -4"
    },
    {
        "category": "Maths",
        "question": "If x = 2 and y = 3, what is (y**y)**x?",
        "choices": ["678", "569", "686", "729"],
        "answer": "729"
    },
    {
        "category": "Maths",
        "question": "What is the square root of 361?",
        "choices": ["19", "48", "29", "9"],
        "answer": "19"
    },
    {
        "category": "Maths",
        "question": "What is the product of 2 ** 8?",
        "choices": ["256", "518", "720", "526"],
        "answer": "256"
    },
    {
        "category": "Maths",
        "question": "If a rectangle has sides of length 4 and 6, what is its perimeter?",
        "choices": ["16", "20", "24", "30"],
        "answer": "20"
    },
    # General Knowledge (GK) Questions
    {
        "category": "GK",
        "question": "What is the capital of India?",
        "choices": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "category": "GK",
        "question": "Who is the Prime Minister of the United Kingdom?",
        "choices": ["Boris Johnson", "Angela Merkel", "Emmanuel Macron", "Justin Trudeau"],
        "answer": "Boris Johnson"
    },
    {
        "category": "GK",
        "question": "In which year did the Titanic sink?",
        "choices": ["1912", "1920", "1930", "1940"],
        "answer": "1912"
    },
    {
        "category": "GK",
        "question": "What is the largest mammal in the world?",
        "choices": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": "Blue Whale"
    },
    {
        "category": "GK",
        "question": "Which planet is known as the 'Red Planet'?",
        "choices": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    # Reasoning Questions
    {
        "category": "Reasoning",
        "question": "If all cats are mammals, and Fluffy is a cat, what can we conclude about Fluffy?",
        "choices": ["Fluffy is a mammal", "Fluffy is not a mammal", "Fluffy is a bird", "Fluffy is a fish"],
        "answer": "Fluffy is a mammal"
    },
    {
        "category": "Reasoning",
        "question": "What comes next in the sequence: 2, 4, 6, 8, ___?",
        "choices": ["10", "12", "14", "16"],
        "answer": "10"
    },
    {
        "category": "Reasoning",
        "question": "If a shirt costs $20 and is on sale for 25% off, what is the discounted price?",
        "choices": ["$5", "$10", "$15", "$18"],
        "answer": "$15"
    },
    {
        "category": "Reasoning",
        "question": "Which of the following is not a prime number: 11, 13, 15, 17?",
        "choices": ["11", "13", "15", "17"],
        "answer": "15"
    },
    {
        "category": "Reasoning",
        "question": "If the day after tomorrow is a Sunday, what day is it today?",
        "choices": ["Monday", "Tuesday", "Wednesday", "Saturday"],
        "answer": "Friday"
    },
    # English Questions
    {
        "category": "English",
        "question": "What is the plural form of 'child'?",
        "choices": ["Children", "Childs", "Childies", "Childs"],
        "answer": "Children"
    },
    {
        "category": "English",
        "question": "Which of the following words is a synonym for 'happy'?",
        "choices": ["Sad", "Joyful", "Angry", "Tired"],
        "answer": "Joyful"
    },
    {
        "category": "English",
        "question": "What is the past tense of the verb 'run'?",
        "choices": ["Running", "Ran", "Runned", "Runs"],
        "answer": "Ran"
    },
    {
        "category": "English",
        "question": "What is the correct spelling of the word 'accommodation'?",
        "choices": ["Acomodation", "Accomodation", "Accommodation", "Acommodation"],
        "answer": "Accommodation"
    },
    {
        "category": "English",
        "question": "In the sentence 'The cat is on the mat,' what is the preposition?",
        "choices": ["The", "Is", "On", "Mat"],
        "answer": "On"
    },
]


# Function to display the current question and choices
def show_question():
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    
    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question +=1

    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
style = Style(theme="flatly")

# Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Create the question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

# Initialize the current question index
current_question = 0

# Show the first question
show_question()

# Start the main event loop
root.mainloop()