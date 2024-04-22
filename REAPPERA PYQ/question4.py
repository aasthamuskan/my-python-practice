def process_medicines(s, k):
    subparts_count = len(s) // k

    for i in range(subparts_count):
        subpart = s[i * k : (i + 1) * k]

        processed_subpart = "".join(sorted(set(subpart), key=subpart.index))

        print(processed_subpart)

s = input().strip()
k = int(input())

process_medicines(s, k)
