has_high_income=True
has_good_credit=False
has_criminal_history=False

'''
if has_high_income and has_good_credit:
    print("Eligible for Loan1")
else:
    print("Improve your credit score")
'''


'''
if has_good_credit and not has_criminal_history:
    print("Eligible for loan2")
'''

if has_high_income or has_good_credit:
    print("Eligible for Loan3")