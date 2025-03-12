import datetime
import os

print("Chatbot: Hello! How can I help you today?")

chat_history = []  # Store chat history

while True:
    user_input = input("User: ").strip().lower()
    chat_history.append(f"User: {user_input}")

    if user_input not in ["hello", "hi", "date", "time", "list", "prime", "history", "bye"]:
        print("Chatbot: Enter correct keyword")
        continue

    if user_input in ["hello", "hi"]:
        print("Chatbot: Hi! How can I help you?")
        chat_history.append("Chatbot: Hi! How can I help you?")

    elif user_input in ["date", "time"]:
        current_time = datetime.datetime.now().strftime("%d %B %Y, %I:%M %p")
        print("Chatbot:", current_time)
        chat_history.append(f"Chatbot: {current_time}")

    elif user_input == "list":
        try:
            numbers = list(map(int, input("Enter numbers (comma-separated): ").split(',')))
            result = f"Sum: {sum(numbers)}, Max: {max(numbers)}, Reversed: {numbers[::-1]}"
            counts= {num: sum(1 for n in numbers if n==num) for num in set(numbers)}
            print(counts)
            print(result)
            chat_history.append(f"Chatbot: {result}")

            if input("Remove duplicates? (yes/no): ").strip().lower() == "yes":
                updated_list = sorted(set(numbers))
                print("Updated List:", updated_list)
                chat_history.append(f"Chatbot: Updated List: {updated_list}")

        except ValueError:
            print("Error: Enter only numbers separated by commas.")
            chat_history.append("Chatbot: Error: Enter only numbers separated by commas.")

    elif user_input == "prime":
        try:
            start, end = map(int, input("Enter range (start, end): ").split(','))
            primes = [n for n in range(start, end+1) if all(n % i != 0 for i in range(2, int(n**0.5) + 1)) and n > 1]
            print("Prime Numbers:", primes)
            chat_history.append(f"Chatbot: Prime Numbers: {primes}")
        except ValueError:
            print("Error: Enter two numbers separated by a comma.")
            chat_history.append("Chatbot: Error: Enter two numbers separated by a comma.")

    elif user_input == "history":
        keyword = input("Enter keyword to search in history: ").strip().lower()
        matches = [line for line in chat_history if keyword in line.lower()]
        history_output = "Found:\n" + "\n".join(matches) if matches else "No matching history found."
        print(history_output)
        chat_history.append(f"Chatbot: {history_output}")

    elif user_input == "bye":
        # Save history to a file
        history_file = os.path.join("C:\\Users\\poona\\PycharmProjects","chat_history.txt")
        with open(history_file, "w", encoding="utf-8") as file:
            file.write("\n".join(chat_history))

        print(f"Chatbot: Chat history saved to '{history_file}'")
        print("Chatbot: Goodbye! Have a great day!")
        break

