annual_salary=int(input('The starting annual salary is: '))
portion_saved=float(input('The portion to be saved: '))
total_cost=int(input('Total cost of your dream home: '))
n=0 #total number of months required to save enough money to buy the house
r=0.04
pdp=0.25 #portion down payment
down_payment=pdp*(total_cost)
total_savings=0
current_savings=0
while total_savings< down_payment:
    current_savings= portion_saved*(annual_salary/12)+total_savings*(r/12)
    total_savings=total_savings+current_savings
    n=n+1
print('Number of months: ',n)

