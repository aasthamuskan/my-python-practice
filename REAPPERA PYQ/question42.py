def get_month_name(number):
    if 1 <= number <= 12:
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return months[number - 1]
    else:
        return "Invalid"

if __name__ == "__main__":
    input_number = int(input("Enter an integer: "))
    result_month = get_month_name(input_number)

    print(result_month)
