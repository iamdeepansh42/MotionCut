def count_words():
    # Prompt the user to enter a sentence or paragraph
    print("Please enter a sentence or paragraph:")

    # Get the user input
    user_input = input()

    # Error handling for empty input
    if not user_input:
        print("You entered an empty string. Please enter a sentence or paragraph.")
        return

    # Count the number of words in the input
    word_count = len(user_input.split())

    # Print the word count to the console
    print(f"The number of words in your input is: {word_count}")

# Ensure a clear and user-friendly interface for input and output
if __name__ == "__main__":
    count_words()
