int_list = [12, 5, 8, 20, 3, 15, 7, 10, 18, 1]

print("Original list:")
for num in int_list:
    print(num, end=" ")
print("\n")

print("Highest value:", max(int_list))
print("Lowest value:", min(int_list))
print()

int_list.sort()
print("Sorted in ascending order:", int_list)

int_list.sort(reverse=True)
print("Sorted in descending order:", int_list)

int_list.append(25)
int_list.append(6)
print("\nList after appending 25 and 6:", int_list)
