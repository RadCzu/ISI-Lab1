statement = input("Write something: ")

spaceless_statement = statement.replace(" ", "")
# spaceless_statement = "".join(statement.split())
if spaceless_statement[::-1] == spaceless_statement:
    print(f"{statement} is a palindrome")
else:
    print(f"{statement} is not a palindrome")