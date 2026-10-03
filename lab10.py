name = input("Enter your name: ")
dept = input("Enter your department: ")
score_1 = int(input("Enter the first score: "))
score_2 = int(input("Enter the second score: "))
score_3 = int(input("Enter the third score: "))
score_list = [score_1, score_2, score_3]
score_list_len = len(score_list)
total_score = score_1 + score_2 + score_3
average_score = total_score / score_list_len
grade = ""

def calculate_grade(average_score):
    if average_score >= 70:
        return "A"
    elif average_score >= 60:
        return "B"
    elif average_score >= 50:
        return "C"
    elif average_score >= 45:
        return "D"
    else:
        return "F"

grade = calculate_grade(average_score)

store_details = {
    "Name": name,
    "Dept": dept,
    "Scores": score_list,
    "Total": total_score,
    "Average": average_score,
    "Grade": grade
}

print("\n==== STUDENT REPORT ====\n")

for key in store_details:
    print(f"{key}: {store_details[key]}")