def analyze(salary):
    
    avg = sum(salary) / len(salary)
    print(f"Average Salary: {avg:.2f}")
    
   
    print("Salaries above average:")
    for sal in salary:
        if sal > avg:
            print(sal)
            
   
    updated_salaries = [sal * 1.10 for sal in salary]
    print(f"Salaries after 10% increase: {updated_salaries}")
    
    return updated_salaries


salary = [10000, 20000, 30000, 40000]
updated_salary = analyze(salary)
