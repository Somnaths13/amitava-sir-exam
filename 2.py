'''
Question 2: Online Mobile Store
An online store maintains a list of mobile prices. Write a function
to display all mobiles costing more than ₹20,000, calculate the
total inventory value, and find the most expensive mobile price.
'''
def mobile_price(mobile_prize):
    for i in mobile_prize:
        if i>20000:
            print(i)
    

       
mobile_prize=[21000,34000,15000,17000]
mobile_price(mobile_prize)