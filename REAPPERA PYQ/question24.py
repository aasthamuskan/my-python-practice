def categorize_products(product_ids):
    categorized_ids = []
    for id_num in product_ids:
        if id_num % 5 == 0:
            categorized_ids.append('@')
        elif id_num % 3 == 0:
            categorized_ids.append('#')
        else:
            categorized_ids.append('*')
    return categorized_ids

# Example Usage
if __name__ == "__main__":
    input_ids = list(map(int, input("Enter product IDs separated by commas: ").split(',')))
    updated_ids = categorize_products(input_ids)
    print(updated_ids)
