# Quiz Application

This is a Python-based quiz application that fetches trivia questions from the Open Trivia Database (OpenTDB) API. Users can select from different categories and difficulty levels to answer True/False questions.

## Project Structure

The project consists of three Python files:
1. **`question_model.py`**: Defines the `Question` class to hold question text and correct answers.
2. **`brain.py`**: Contains the `QuizBrain` class, which handles the quiz logic (asking questions, checking answers, and tracking score).
3. **`quiz.py`**: Main script to run the quiz. It fetches the questions from the OpenTDB API, allows users to select a category and difficulty, and runs the quiz using `QuizBrain`.

## Requirements

This project requires the following libraries:
- `requests` for making API requests to OpenTDB.
- `prettytable` for displaying the list of categories in a table format.

You can install these dependencies using pip.

## How to Run

1. Clone this repository or download the files.
2. Install the required dependencies by running:
```bash
pip install requests prettytable
```
3. Run the quiz.py file:
```bash
python quiz.py
```
4. Follow the prompts to select a category and difficulty level. Answer the True/False questions to complete the quiz.

## Example Output
```bash
+-----------------------+-------+
|        Category        | Input |
+-----------------------+-------+
|   General Knowledge    |   9   |
|          Books         |  10   |
|          Film          |  11   |
|          Music         |  12   |
|   Musicals & Theatres  |  13   |
|       Television       |  14   |
|      Video Games       |  15   |
|      Board Games       |  16   |
|   Science & Nature     |  17   |
|       Computers        |  18   |
|      Mathematics       |  19   |
|       Mythology        |  20   |
|         Sports         |  21   |
|       Geography        |  22   |
|        History         |  23   |
|        Politics        |  24   |
|          Art           |  25   |
|      Celebrities       |  26   |
|        Animals         |  27   |
|       Vehicles         |  28   |
|        Comics          |  29   |
|        Gadgets         |  30   |
|   Japanese Anime       |  31   |
| Cartoon & Animations   |  32   |
+-----------------------+-------+

Enter the category number: 9
You have chosen topic 9.
Choose difficulty (easy, medium, hard): easy
You have chosen easy difficulty.

Q.1: Is the sky blue? (True/False):
```

## Features

- Fetches 10 True/False questions based on the user's selected category and difficulty.
- Tracks the user's score and provides feedback after each question.
- Displays the user's final score at the end of the quiz.

## Code Overview

**`question_model.py`**
- This file contains the `Question` class, which represents a question in the quiz

**`brain.py`**
- The QuizBrain class manages the quiz's flow and logic:
  - `next_question()`: Asks the next question and verifies the user's input.
  - `still_has_questions_left()`: Checks if there are more questions in the quiz.
  - `check_answer()`: Compares the user's answer with the correct answer and updates the score.

**`quiz.py`**
- The main script that:
  - Fetches questions using the OpenTDB API.
  - Prompts the user to select a category and difficulty.
  - Runs the quiz loop using the QuizBrain class.
 
## Future Improvements

- Add support for multiple question types (e.g., multiple choice).
- Allow users to customize the number of questions fetched.
- Improve input validation and error handling.
- Enhance the user interface for a more interactive experience.





