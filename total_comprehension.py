# total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

# TODO: write python code here

print("--------------")
#MAPPED LIST: [100, 200, 300, 400, 500, 600, 700]
#mapped_list = [m * 100 for m in my_numbers]
#
#LIST COMPREHENSION = SHORT WAY
#

mapped_list = [i * 100 for i in my_numbers]

print("MAPPED LIST: ", mapped_list)

#
#LONG WAY
#

new_numbers = []

for i in my_numbers:
    new_numbers.append(i * 100)

print("MAPPED LIST: ", new_numbers)

#
# LONG WAY
#
filtered_list =[]
for x in my_numbers:
    if x > 3:
        filtered_list.append(x)
print("FILTERED LIST:", filtered_list)

print("--------------")
#FILTERED LIST W/ MATCHES: [4, 5, 6, 7]
#LIST COMPREHENSION: SHORT WAY
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
