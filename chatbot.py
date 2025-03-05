import datetime

# Chatbot start
print("Chatbot: Hello! How can I help you today?")

while True:
    user_input = input("User: ").strip().lower()

    # Check for valid keywords
    if user_input not in ["hello", "hi", "date", "time", "list", "prime", "history", "bye"]:
        print("Chatbot: Please Enter correct keyword")
        continue


    if user_input in ["hello", "hi"]:
        print("Chatbot: Hi! How can I help you?")

    # Date and Time
    elif user_input in ["date", "time"]:
        print("Chatbot:", datetime.datetime.now().strftime("%d %B %Y, %I:%M %p"))

    # List Operations
    elif user_input == "list":
        try:
            numbers = list(map(int, input("Enter numbers (comma-separated): ").split(',')))
            print(f"Sum: {sum(numbers)}")
            print(f"Max: {max(numbers)}")
            print(f"Reversed: {numbers[::-1]}")
        except ValueError:
            print("Error: Enter only numbers separated by commas.")

    # Prime Number Generation
    elif user_input == "prime":
        try:
            start, end = map(int, input("Enter range (start, end): ").split(','))
            primes = [num for num in range(start, end + 1) if all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1]
            print("Prime Numbers:", primes)
        except ValueError:
            print("Error: Enter two numbers separated by a comma.")

    # Search History
    elif user_input == "history":
        print("Chatbot: This feature is under development.")

    # Exit Chatbot    elif user_input == "bye":

        print("Chatbot: Goodbye! Have a great day!")
        break

