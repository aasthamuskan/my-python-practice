def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def categorize_books(book_ids):
    categorized_ids = []
    for book_id in book_ids:
        if book_id % 2 != 0:
            if is_prime(book_id):
                categorized_ids.append('#')
            else:
                categorized_ids.append('')
        else:
            categorized_ids.append(book_id)
    return categorized_ids

# Example Usage
book_ids_input = input().split(',')
book_ids = [int(id_str) for id_str in book_ids_input]
modified_list = categorize_books(book_ids)
print(modified_list)
