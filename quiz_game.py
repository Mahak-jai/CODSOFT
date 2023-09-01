class Question:
    def __init__(self, question, choices, correct_choice=None, fill_in_blank=False):
        self.question = question
        self.choices = choices
        self.correct_choice = correct_choice
        self.fill_in_blank = fill_in_blank

    def display_question(self):
        print(self.question)
        if not self.fill_in_blank:
            for index, choice in enumerate(self.choices, start=1):
                print(f"{index}. {choice}")
        else:
            print("Fill in the blank.")

    def check_answer(self, user_answer):
        if not self.fill_in_blank:
            return user_answer == self.correct_choice
        else:
            return user_answer.lower() in self.correct_choice.lower()

def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for question in questions:
        print("\n")
        question.display_question()

        if question.fill_in_blank:
            user_answer = input("Your answer: ")
        else:
            user_choice = int(input("Enter your choice (1/2/3): ")) - 1
            user_answer = question.choices[user_choice]

        if question.check_answer(user_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question.correct_choice)

    print("\nQuiz completed!")
    print(f"You scored {score} out of {total_questions}.")
    if(score==7):
        print("You Have Won the Quiz")
    else:
        print("You Have lost the Quiz...Thanks for your Participation")

def main():
    question1 = Question(
        "What is the capital of France?",
        ["Paris", "Berlin", "Madrid"],
        "Paris"
    )

    question2 = Question(
        "Which planet is known as the Red Planet?",
        ["Mars", "Venus", "Jupiter"],
        "Mars"
    )

    question3 = Question(
        "What is the largest mammal?",
        ["Blue Whale", "African Elephant", "Giraffe"],
        "Blue Whale"
    )

    question4 = Question(
        "The Earth revolves around which celestial body?",
        [],
        "Sun",
        fill_in_blank=True
    )

    question5 = Question(
        "Which Country Has the Largest Population in the world?",
        ["India", "China", "USA"],
        "China"
    )

    question6 = Question(
        "Which Planet has the most moons?",
        ["Neptune", "Jupiter", "Saturn"],
        "Saturn"
    )

    question7 = Question(
        "How many planets are there in our solar system?",
        [],
        "Eight",
        fill_in_blank=True
    )

    questions = [question1, question2, question3, question4,question5,question6,question7]
    run_quiz(questions)

if __name__ == "__main__":
    main()
