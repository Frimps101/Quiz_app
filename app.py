"""
A simple python quiz app
https://realpython.com/python-quiz-application/
"""

# !r indicates that answer should be inserted based on its repr() representation. In practice, this means that strings are shown surrounded by single quotes, like '1871'


# answer = input("When was the first known use of the word 'quiz'? ")

# if answer == "1781":
#     print("Correct")
# else:
#     print(f"The answer is '1781' not {answer!r}")
  
  
# answer = input("Which built-in function can get information from the user? ")
# if answer == "input":
#     print("Correct!")
# else:
#     print(f"The answer is 'input', not {answer!r}")

# To obey DRY, a list of tuples is used to hold questions and answers
QUESTIONS =[
    ("When was the first known use of the word 'quiz'", "1781"),
    ("Which built-in function can get information from the user","input")
]

for question, correct_answer in QUESTIONS:
    answer = input(f"{question}?")
    
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r} not {answer!r}")
        
