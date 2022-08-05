a=int(input('The starting annual salary is: '))
total_cost=1000000
semi_annual_raise=0.07
 #total number of months required to save enough money to buy the house
r=0.04
pdp=0.25 #portion down payment
down_payment=pdp*(total_cost)
high=100
low=0
portion_saved=(high+low)/2
while portion_saved>0.1 and portion_saved !=100:
    n=0
    total_savings = 0
    current_savings = 0
    annual_salary=a
    while n<=36:
        current_savings = (portion_saved/100) * (annual_salary / 12) + total_savings * (r / 12)
        total_savings = total_savings + current_savings
        n = n + 1
        if n % 6 == 0:
            annual_salary = annual_salary + semi_annual_raise * (annual_salary)
    if total_savings>down_payment+100:
        high= portion_saved
        portion_saved = (high + low) / 2
    elif total_savings<down_payment-100:
        low=portion_saved
        portion_saved=(high+low)/2
    else:
        break

if abs(down_payment-total_savings)>100:
    print("Down payment is not possible")
else:
    print('best savings rate: ',portion_saved/100)


