# Taking input
sunshine_members = input().split()
rainbow_members = input().split()

# Finding common friends
common_friends = set(sunshine_members) & set(rainbow_members)

# Outputting the common friends
print(", ".join(common_friends))
