'''
Question 1: Student Marks Analysis
A college stores students' marks in a list. Write a function that
accepts a list of marks and displays the highest mark, lowest
mark, average mark, and number of students who passed (marks
of 40 or above).
'''
def marks(marks_list):
    highest=max(marks_list)
    lowest=min(marks_list)
    avg=sum(marks_list)/len(marks_list)

    print(f"highest mark={highest}")
    print(f"lowest mark={lowest}")
    print(f"average mark={avg}")

marks_list=[10,20,30,40,50,60]
marks(marks_list)

