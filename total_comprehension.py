# total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

# TODO: write python code here

print("--------------")
#MAPPED LIST: [100, 200, 300, 400, 500, 600, 700]
mapped_list = [m * 100 for m in my_numbers]
print("MAPPED LIST: ", mapped_list)
print("--------------")
#FILTERED LIST W/ MATCHES: [4, 5, 6, 7]
filtered_list = [m for m in my_numbers if m > 3]
print("FILTERED LIST W/ MATCHES: ", filtered_list)
print("--------------")
#FILTERED LIST W/O MATCHES: []
no_matches = [m for m in my_numbers if m > 8]
print("FILTERED LIST W/O MATCHES: ", no_matches)

print("--------------")
#MAPPED AND FILTERED LIST: [400, 500, 600, 700]
mapped_and_filtered = [m * 100 for m in my_numbers if m > 3]
print("MAPPED AND FILTERED LIST: ", mapped_and_filtered)
