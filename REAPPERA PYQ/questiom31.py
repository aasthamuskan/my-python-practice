def find_weekday(day_number):
    weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if day_number >= 1 and day_number <= 7:
        return weekdays[day_number - 1]
    else:
        return 'Invalid'

# Example Usage
day_number = int(input("Enter an integer (1-7): "))
weekday_name = find_weekday(day_number)
print(weekday_name)
