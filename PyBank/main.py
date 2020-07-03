import os
import csv
import math

csvpath = os.path.join('Resources', 'budget_data.csv')


input_file = csv.DictReader(open(csvpath))

total_line = 0
total_amount = 0
total_avr = 0
max_num = 0
low_num = 0
current_date = None
current_date2 = None  
for row in input_file:
    num = int(row['Profit/Losses'])
    date = str(row['Date'])
    total_line += 1
    total_amount += num  
    if max_num == max_num < num:
        max_num = num
        current_date = date
    if low_num == low_num > num:
        low_num = num
        current_date2 = date

total_avr = total_line/total_amount

        
print('\nFinancial Analysis')
print('------------------------------')
print(f'\nTotal Months:{total_line}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${total_avr}')
print(f'Greatest Increase in Profits: {current_date} (${max_num})')
print(f'Greatest Decrease in Profits: {current_date2} (${low_num})')

with open('pybank_output.txt', 'w') as text:
    text.write('Financial Analysis')
    text.write('\n------------------------------')
    text.write(f'\nTotal Months:{total_line}')
    text.write(f'\nTotal: ${total_amount}')
    text.write(f'\nAverage Change: ${total_avr}')
    text.write(f'\nGreatest Increase in Profits: {current_date} (${max_num})')
    text.write(f'\nGreatest Decrease in Profits: {current_date2} (${low_num})')