'''
Question 8: Student Registration Record
A college stores a student's roll number, name, course, and
semester in a tuple. Write a function that displays each field
separately and prints the complete student record.
'''
def display_student_record(student_tuple):
   
    roll_number, name, course, semester = student_tuple
    
    
    print("--- Individual Fields ---")
    print(f"Roll Number: {roll_number}")
    print(f"Name       : {name}")
    print(f"Course     : {course}")
    print(f"Semester   : {semester}")
    print("-------------------------")
    
   
    print(f"Complete Student Record: {student_tuple}")


student_data = (101, "Aman Sharma", "B.Tech Computer Science", "3rd Semester")


display_student_record(student_data)
