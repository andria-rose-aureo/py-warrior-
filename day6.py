
marks = [45, 78, 90, 34, 67]
def mark():
    print(f"student marks list {marks}")

def updated_marks():
    mark()
    index = int(input("Which student's mark do you want to update? Enter Index:"))
    new_mark = input("Enter New Mark:")
    marks[index] = new_mark
    print(f"updated list {marks}")

updated_marks()
