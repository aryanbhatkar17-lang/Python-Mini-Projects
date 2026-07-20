import time
import random

def get_questions():
    return [
    {
        "question": "What is the correct file extension for Python files?",
        "options": ["A. .py", "B. .pyt", "C. .pyw", "D. .pt"],
        "answer": "A"
    },
    {
        "question": "Which of the following is an invalid variable name in Python?",
        "options": ["A. my_var", "B. _myvar", "C. 2myvar", "D. myVar"],
        "answer": "C"
    },
    {
        "question": "How do you create a variable with the floating-point number 2.8?",
        "options": ["A. x = float(2.8)", "B. x = 2.8", "C. Both A and B", "D. None of the above"],
        "answer": "C"
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["A. 5", "B. 6", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "Which method can be used to return a string in upper case?",
        "options": ["A. upper()", "B. uppercase()", "C. toUpperCase()", "D. up()"],
        "answer": "A"
    },
    {
        "question": "Which collection is ordered, changeable, and allows duplicate members?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "A"
    },
    {
        "question": "Which collection does NOT allow duplicate members?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. All of the above"],
        "answer": "C"
    },
    {
        "question": "How do you start writing a 'for' loop in Python?",
        "options": ["A. for x in y:", "B. for x to y:", "C. for each x in y:", "D. for (x; x < y; x++)"],
        "answer": "A"
    },
    {
        "question": "Which of the following is used to define a block of code in Python?",
        "options": ["A. Curly braces", "B. Parentheses", "C. Indentation", "D. Quotations"],
        "answer": "C"
    },
    {
        "question": "What is the output of print(type([]) )?",
        "options": ["A. <class 'tuple'>", "B. <class 'list'>", "C. <class 'set'>", "D. <class 'dict'>"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. void", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "How do you insert an element at a specific index in a list?",
        "options": ["A. insert()", "B. add()", "C. append()", "D. push()"],
        "answer": "A"
    },
    {
        "question": "What is the output of print(len('Python'))?",
        "options": ["A. 5", "B. 6", "C. 7", "D. Error"],
        "answer": "B"
    },
    {
        "question": "Which of the following statements is used to import a module in Python?",
        "options": ["A. require", "B. include", "C. import", "D. using"],
        "answer": "C"
    },
    {
        "question": "How do you write a comment in Python?",
        "options": ["A. // This is a comment", "B. /* This is a comment */", "C. # This is a comment", "D. <!-- This is a comment -->"],
        "answer": "C"
    },
    {
        "question": "What is the output of 10 // 3 in Python?",
        "options": ["A. 3.3333", "B. 3", "C. 1", "D. 3.0"],
        "answer": "B"
    },
    {
        "question": "Which method is used to remove whitespace from both the beginning and the end of a string?",
        "options": ["A. strip()", "B. trim()", "C. len()", "D. remove()"],
        "answer": "A"
    },
    {
        "question": "How do you handle potential exceptions in Python?",
        "options": ["A. try/except", "B. try/catch", "C. do/catch", "D. throw/catch"],
        "answer": "A"
    },
    {
        "question": "What does the 'range(5)' function generate?",
        "options": ["A. Numbers from 1 to 5", "B. Numbers from 0 to 4", "C. Numbers from 0 to 5", "D. Numbers from 1 to 4"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to return a value from a function?",
        "options": ["A. give", "B. break", "C. return", "D. yield"],
        "answer": "C"
    }
]

def countdown_timer():
    
    for i in range(10, -1, -1):
        print(f"\r You have {i} seconds to answer the question    ", end="")
        time.sleep(1)
    print("\n")


def display_questions(question, i):
    print("--------------------------------------------------")
    print(f"{i}. {question["question"]}")
    for option in question["options"]:
        print(option)


def get_user_choice():
    choice = input("Enter your answer (A, B, C, D) :").strip().upper()
    if choice in ["A", "B", "C", "D"]:
        return choice
    else:
        return None


def check_answer(choice, answer):
    if choice == answer:
        print("Your answer is correct")
        return 1
    else:
        print("Your answer is wrong!, The correct answer is: " + answer )
        return 0
    

def update_score(result, score):
    if result:
        score +=1
    return score


def play_quiz():
    print("Welcome to the QUiz game!!!")

    questions = get_questions()

    random.shuffle(questions)
    score =0
    i = 1

    for question in questions:
        display_questions(question, i)
        countdown_timer()
        choice = get_user_choice()
        result = check_answer(choice, question["answer"])
        score =update_score(result, score)
        i = i+1

    print(f"Your score is {score}/{len(questions)}")
    print("Thanks for Playing")


if __name__ == "__main__":
    play_quiz()

