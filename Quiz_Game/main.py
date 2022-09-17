from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dictionary in question_data:
    # Save the values of the text key and answer key 
    text = dictionary["question"]
    answer = dictionary["correct_answer"]
    # Create Question object
    question = Question(text, answer)
    # Add the object to the question_bank list
    question_bank.append(question)

# print(question_bank) outputs a list of memory addresses that the objects point to
# print(question_bank[0].answer) outputs the actual True answer pointed at

# Create object of QuizBrain class
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}.")

