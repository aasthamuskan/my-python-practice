def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def check_room_prime(room_number):
    if is_prime(room_number):
        print(room_number, "is prime")
    else:
        print(room_number, "is not prime")

# Example Usage
if __name__ == "__main__":
    room_number = int(input("Enter the room number (0 < room number < 500): "))
    check_room_prime(room_number)
