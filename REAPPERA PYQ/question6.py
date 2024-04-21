class Customer:
    def __init__(self, name, total_purchase):
        self.__name = name
        self.__total_purchase = total_purchase

    def get_name(self):
        return self.__name

    def get_total_purchase(self):
        return self.__total_purchase

    def apply_fee(self, fee_percentage):
        if fee_percentage < 0 or fee_percentage > 15:
            return "Invalid fee percentage"
        else:
            total_with_fee = self.__total_purchase * (1 + fee_percentage / 100)
            return total_with_fee

name = input()
total_purchase = float(input())
fee_percentage = float(input())

obj = Customer(name, total_purchase)

print(obj.get_name())
print(obj.get_total_purchase())

result = obj.apply_fee(fee_percentage)
print(result)
