s = input("Enter a word or number: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")