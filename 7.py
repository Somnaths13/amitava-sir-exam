'''
Question 7: Daily Expense Tracker
A person records daily expenses in a list. Write a function to
calculate the total expenses, average daily expense, and the days
on which expenses exceeded ₹1,000.
'''
def expense_tracker(expenses):
    total=0
    high_days = []
    day_number = 1
    
    for amount in expenses:
        total = total + amount  
        
        if amount > 1000:
            high_days.append(day_number) 
            
        day_number = day_number + 1  

    
    average = total / len(expenses)

    
    print("Total Expenses: ", total)
    print("Average Daily Expense: ", average)
    print("Days where expense exceeded 1,000:", high_days)

daily_expenses = [450, 1200, 800, 2500, 950, 1100, 600]
expense_tracker(daily_expenses)