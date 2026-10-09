'''
Question 6: Hospital Patient Queue
A hospital maintains a list of patients waiting for consultation.
Write a function that removes the first patient after consultation,
adds a new patient to the queue, and displays the updated queue.
'''
def patient_queue(patients):
 
    if patients:
        removed_patient = patients.pop(0)
        print("Consultation completed for:", removed_patient)

   
    new_patient = input("Enter the new patient's name: ")
    patients.append(new_patient)

    
    print("Updated patient queue:", patients)


patients = ["Rahul", "Priya", "Amit", "Sneha"]
patient_queue(patients)