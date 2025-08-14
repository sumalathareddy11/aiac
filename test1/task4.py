def process_text():
    import string

    # Define a simple list of English stop words
    stop_words = {
        'a', 'an', 'the', 'and', 'or', 'but', 'if', 'while', 'with', 'to', 'of', 'at', 'by', 'for', 'from', 'in', 'on', 'off', 'out', 'over', 'under', 'as', 'is', 'it', 'this', 'that', 'these', 'those', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'so', 'such', 'no', 'not', 'too', 'very', 'can', 'will', 'just'
    }

    text = input("Enter a string: ")
    # Remove punctuation
    text_no_punct = text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    text_lower = text_no_punct.lower()
    # Split into words
    words = text_lower.split()
    # Remove stop words
    filtered_words = [word for word in words if word not in stop_words]
    # Join back to string
    output = ' '.join(filtered_words)
    print(output)

process_text()


