Hours = float(input('Enter Hours: '))
Rate = float(input('Enter Rate: '))
if Hours > 40:
    overtime = Hours - 40
    Pay = (40 * Rate) + (overtime * Rate * 1.5)
else: Pay = Hours * Rate
print('Pay: ', Pay)