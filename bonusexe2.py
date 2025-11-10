locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

print("Original list:", locations)

print("Length of list:", len(locations))
print()

print("Alphabetical order (using sorted):", sorted(locations))

print("Original list after sorted():", locations)
print()

print("Reverse alphabetical order (using sorted with reverse=True):", sorted(locations, reverse=True))

print("Original list after reverse sorted():", locations)
print()

locations.reverse()
print("List after using reverse():", locations)
print()

locations.sort()
print("List after using sort() (alphabetical):", locations)
print()

locations.sort(reverse=True)
print("List after using sort(reverse=True):", locations)

