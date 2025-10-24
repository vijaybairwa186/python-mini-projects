# --> Who wants to be a Millionaire Game

questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
]

prizes = [100000, 320000, 400000, 450000, 500000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000]

total_won = 0

print("\nWelcome to the Quiz Game!")
print("Answer the questions correctly to win exciting prizes \n")

for i, question in enumerate(questions):
    print(f"Question {i+1}: {question[0]}")
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    try:
        ans = int(input("Enter your answer (1 for a, 2 for b, 3 for c, 4 for d): "))
        
        if ans < 1 or ans > 4:
            print("Invalid choice! Please enter a number between 1 and 4.")
            continue

        if question[5] == ans:
            print("Correct Answer!")
            total_won = prizes[i]
            print(f"You won ₹{prizes[i]:,}\n")
        else:
            print(f"Incorrect! The correct answer was option {question[5]} ({question[question[5]]})")
            print(f"You take home ₹{total_won:,}")
            break

    except ValueError:
        print("Please enter a valid number (1–4)!\n")

else:
    print(f"Congratulations! You completed all questions and won ₹{total_won:,}!")

print("\nThanks for playing the Quiz Game!")
