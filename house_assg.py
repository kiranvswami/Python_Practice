price=50000
has_good_credit=False

if has_good_credit:
	down_payment=price*0.1

else:
	down_payment=price*0.2

print(f"Your downpayment amount is: ₹{down_payment}")