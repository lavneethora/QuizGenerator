from question_model import Question
from brain import QuizBrain
import requests
import prettytable

def fetch_questions(category, difficulty):
    url = f"https://opentdb.com/api.php?amount=10&category={category}&difficulty={difficulty}&type=boolean"
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    question_bank = []
    for item in data["results"]:
        question_text = item["question"]
        question_answer = item["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    
    return question_bank

def get_user_choices():
    categories = prettytable.PrettyTable()
    categories.add_column('Category', ['General Knowledge', 'Books', 'Film', 'Music', 'Musicals & Theatres',
                            'Television', 'Video Games', 'Board Games', 'Science & Nature', 'Computers',  
                            'Mathematics', 'Mythology', 'Sports', 'Geography', 'History', 'Politics', 'Art',
                            'Celebrities', 'Animals', 'Vehicles', 'Comics', 'Gadgets', 'Japanese Anime', 
                            'Cartoon & Anime'])
    categories.add_column('Input', ['9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                            '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32'])
    print(categories)
    print("\n")
    category = int(input("Enter the category number: "))
    if category < 9 and category > 32:
        print("Invalid category. Please enter a number from the list.")
        return get_user_choices()
    else:
        print(f"You have chosen topic {category}.")
        
    difficulty = input("Choose difficulty (easy, medium, hard): ")
    if difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid difficulty. Please choose 'easy', 'medium', or 'hard'.")
        return get_user_choices()
    else:
        print(f"You have chosen {difficulty} difficulty.")
    
    return category, difficulty

category, difficulty = get_user_choices()
question_bank = fetch_questions(category, difficulty)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions_left():
    quiz.next_question()

print("You have completed the quiz!!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
