date = input("enter date of your birth dd//mm/yyyy:")
cur_date = input("enter the current date dd//mm/yyyy:")
days, month, year = date.split('/')
total_1 = int(year)*365+int(month)*30+int(days)
days, month, year = cur_date.split('/')
total_2 = int(year)*365 + int(month)*30 + int(days)
your_year = (total_2 - total_1)//365
your_day = (total_2 - total_1)%365
print("You are full",your_year,"yars old","and",your_day,"days")