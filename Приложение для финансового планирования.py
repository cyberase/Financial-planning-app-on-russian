wage = int(input('Введите заработную плату в месяц: '))
mortgageinterest = int(input('Введите, какой процент(%) уходит на ипотеку: '))
interestonlife = int(input('Введите, какой процент(%) уходит на жизнь: '))
spentonthemortgage = (wage * mortgageinterest * 12) / 100  
savings = (wage * 12 * (100 - mortgageinterest - interestonlife)) / 100
print('На ипотеку было потрачено: ', spentonthemortgage)
print('Было накоплено: ', savings)