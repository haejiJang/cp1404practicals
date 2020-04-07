"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():
    '''This function asks a score and return the grade'''
    score = float(input("Enter score: "))
    print(evaluate_grade(score))

def evaluate_grade(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score < 50:
        return "Bad"
    elif score >= 50 and score < 90:
        return "Passable"
    elif score >= 90:
        return "Excellent"


main()