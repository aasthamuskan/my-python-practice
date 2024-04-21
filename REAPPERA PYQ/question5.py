def month_name(month):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    if month > 12:
        print("Invalid")
    else:
        print(months[month])

# Taking input
month = int(input())

# Outputting the name of the month
month_name(month)
