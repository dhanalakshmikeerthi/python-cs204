try:
    num=int(input("enter a number:"))
    print(f"you entered:{num}")

except ValueError:
    print("That's not valid!please enter number")
print("program continous after try except block.")
