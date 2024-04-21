class FeeCalculator:
    def __init__(self):
        self.name = ""
        self.roll_number = 0
        self.basic_fee = 0
        self.attendance_percentage = 0.0

    def set_details(self, name, roll_number, basic_fee, attendance_percentage):
        self.name = name
        self.roll_number = roll_number
        self.basic_fee = basic_fee
        self.attendance_percentage = attendance_percentage

    def total_fee(self):
        if self.attendance_percentage <= 50:
            return self.basic_fee + 0.2 * self.basic_fee
        elif self.attendance_percentage > 50 and self.attendance_percentage <= 75:
            return self.basic_fee + 0.15 * self.basic_fee
        else:
            return self.basic_fee

# Example Usage
if __name__ == "__main__":
    calc = FeeCalculator()
    name = input()
    roll_number = int(input())
    basic_fee = int(input())
    attendance_percentage = float(input())
    
    calc.set_details(name, roll_number, basic_fee, attendance_percentage)
    total_fee = calc.total_fee()
    print(total_fee)
