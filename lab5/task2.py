def analyze_sentiment():
    positive_words = {'good', 'great', 'awesome', 'fantastic', 'excellent', 'amazing', 'happy', 'love', 'wonderful', 'best', 'enjoyed', 'nice'}
    negative_words = {'bad', 'worst', 'terrible', 'awful', 'sad', 'hate', 'horrible', 'poor', 'disappointing', 'boring', 'dislike'}
    
    text = input("Enter a sentence to analyze sentiment: ").lower()
    words = set(text.split())
    
    pos_count = len(positive_words & words)
    neg_count = len(negative_words & words)
    
    if pos_count > neg_count:
        sentiment = "positive"
    elif neg_count > pos_count:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    print(f"Identified sentiment: {sentiment}")

# Example usage
if __name__ == "__main__":
    analyze_sentiment()
