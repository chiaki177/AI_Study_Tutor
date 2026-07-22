def score(question, line):
    line_score = 0
    question_split = question.lower().split()
    line_split = line.lower().split()

    for question_words in question_split:

        if question_words in line_split:
            line_score += 1 
        else: 
            continue
    return line_score

