def process_scores(scores):
    avg = sum(scores) / len(scores)
    print("Average score:", avg)
    print("High scores:",max(scores))
    print("Low scores:",min(scores))

process_scores([85, 90, 78, 92, 88])