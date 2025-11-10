year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

print("Value at index -3:", year[-3])

reversed_year = year[::-1]
print("Original tuple:", year)
print("Reversed tuple:", reversed_year)

count_2009 = year.count(2009)
print("Number of times 2009 appears:", count_2009)

index_2018 = year.index(2018)
print("Index of 2018:", index_2018)

length = len(year)
print("Length of the tuple:", length)
