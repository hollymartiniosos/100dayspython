from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# question_bank = [Question(item['text'], item['answer']) for item in question_data]

question_bank =[]

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

# print(question_bank)    
# print([q.text for q in question_bank])

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():               
    quiz.next_question()

print("You've completed the Quiz")
print(f'Your final score was: {quiz.score}/{len(quiz.question_list)}')