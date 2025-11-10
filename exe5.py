count = 0  
choice = input("Would you like to continue? (Y/N): ").upper()

while choice == 'Y':
    count += 1
    print("Loop executed", count, "time(s).")
    choice = input("Would you like to continue? (Y/N): ").upper()

print("\nThe loop was executed", count, "time(s) in total.")
print("Program terminated.")
