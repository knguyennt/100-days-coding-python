print('Welcome to the tip calculator')
total_bill = input('What was the total bill? ')
tip = input('What percentage tip would you like to give? 10, 12, or 15? ')
num_people = input('How many people to split the bill? ')

pay_per_person = (float(total_bill) +  float(total_bill) * int(tip) / 100) / int(num_people)
print(f'each person should pay: ${round(pay_per_person,2)}')