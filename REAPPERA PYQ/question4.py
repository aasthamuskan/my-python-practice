def process_medicines(s, k):
    # Determine the total number of subparts
    subparts_count = len(s) // k

    # Process each subpart
    for i in range(subparts_count):
        # Get the current subpart
        subpart = s[i * k : (i + 1) * k]

        # Remove duplicates while maintaining original sequence
        processed_subpart = "".join(sorted(set(subpart), key=subpart.index))

        # Print the processed subpart
        print(processed_subpart)

# Taking input
s = input().strip()
k = int(input())

# Process the medicines
process_medicines(s, k)
