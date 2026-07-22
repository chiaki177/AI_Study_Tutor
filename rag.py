from scoring import score


def load_knowledge():
    with open("knowledge.txt","r") as file:
        return file.read()
    
def retrieve(question, knowledge):
    highest_score = 0
    for line in knowledge.splitlines():
        current_line_score = score(question, line)
        if current_line_score >= highest_score:
            best_line = line
            highest_score = current_line_score
        else:
            continue
    if highest_score == 0:
        best_line = "No relevant knowledge found."
    return best_line



        
