#price of a house is $1M. If buyer has good credit, they  need to put down  10% otherise
#they need to put down 20%. print the down payment
price=1000000
good_credit= True

if good_credit:
    down_payment=10/100*price
else:
    down_payment=20/100*price
print(f'down payment is ${down_payment}')