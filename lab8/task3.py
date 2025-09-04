import string

def is_sentence_palindrome(sentence):
    # Remove punctuation, spaces, and convert to lowercase
    cleaned = ''.join(
        ch.lower() for ch in sentence if ch.isalnum()
    )
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    print("Check if your own sentence is a palindrome (ignoring case, spaces, and punctuation):")
    user_input = input("Enter a sentence: ")
    if is_sentence_palindrome(user_input):
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")