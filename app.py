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
# QUESTIONS =[
#     ("When was the first known use of the word 'quiz'", "1781"),
#     ("Which built-in function can get information from the user","input")
# ]

# for question, correct_answer in QUESTIONS:
#     answer = input(f"{question}?")
    
#     if answer == correct_answer:
#         print("Correct!")
#     else:
#         print(f"The answer is {correct_answer!r} not {answer!r}")
        

# QUESTIONS = {
#     "When was the first known use of the word 'quiz'": [
#         "1781", "1771", "1871", "1881"
#     ],
#     "Which built-in function can get information from the user": [
#         "input", "get", "print", "write"
#     ],
#     "Which keyword do you use to loop over a given list of elements": [
#         "for", "while", "each", "loop"
#     ],
#     "What's the purpose of the built-in zip() function": [
#         "To iterate over two or more sequences at the same time",
#         "To combine several strings into one",
#         "To compress several files into one archive",
#         "To get information from the user",
#     ],
# }

# for question, alternatives in QUESTIONS.items():
#     correct_answer = alternatives[0]
#     for alternative in sorted(alternatives):
#         print(f"  - {alternative}")

#     answer = input(f"{question}? ")
#     if answer == correct_answer:
#         print("Correct!")
#     else:
#         print(f"The answer is {correct_answer!r}, not {answer!r}")

# Adding the enumerate() function to make the app more forgiving
# By adding a label to the answer
# ie Update the application to use enumerate() to print the index of each answer alternative:

# Update the application to use enumerate() to print the index of each answer alternative

QUESTIONS = {
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop"
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ],
}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives):
        print(f" {label}) {alternative}")
        
    answer_label = int(input(f"{question}?"))
    answer = sorted_alternatives[answer_label]
    if answer == correct_answer:
        print("Correct")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")