def check_voting_eligibility(age, is_citizen):
    """
    Check if a person is eligible to vote based on age and citizenship.

    Parameters:
    age (int): The age of the person.
    is_citizen (bool): Whether the person is a citizen.

    Returns:
    str: A message indicating whether the person is eligible to vote.
    """
    if age >= 18 and is_citizen:
        return "You are eligible to vote."
    elif age < 18 and is_citizen:
        return "You are not eligible to vote because you are under 18."
    elif age >= 18 and not is_citizen:
        return "You are not eligible to vote because you are not a citizen."
    else:
        return "You are not eligible to vote because you are under 18 and not a citizen."
# Example usage:
age = 20
is_citizen = True
result = check_voting_eligibility(age, is_citizen)
print(result)  # Output: You are eligible to vote.
# Explanation of conditions:
# 1. If the person is 18 or older and is a citizen, they are eligible to vote.
# 2. If the person is under 18 but is a citizen, they are not eligible due to age.
# 3. If the person is 18 or older but not a citizen, they are not eligible due to citizenship.
# 4. If the person is under 18 and not a citizen, they are not
#    eligible due to both age and citizenship.

"""Generate Python code to count vowels and consonants in a string
using a loop.”
Expected Output:
• AI-generated string processing logic.
• Correct counts.
• Output verification."""
def count_vowels_and_consonants(input_string):
    """
    Count the number of vowels and consonants in a given string.

    Parameters:
    input_string (str): The string to be analyzed.

    Returns:
    tuple: A tuple containing the count of vowels and consonants.
    """
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count
# Example usage:
input_string = "Hello World"
vowels, consonants = count_vowels_and_consonants(input_string)
print(f"Vowels: {vowels}, Consonants: {consonants}")  # Output: Vowels: 3, Consonants: 7
# Explanation:
# The function iterates through each character in the input string.
# It checks if the character is an alphabet letter.
# If it is a vowel (present in the vowels string), it increments the vowel count.
# If it is a consonant, it increments the consonant count.
# Finally, it returns the counts of vowels and consonants.

"""Generate a Python program for a library management system
using classes, loops, and conditional statements.”
Expected Output:
• Complete AI-generated program.
• Review of AI suggestions quality.
• Short reflection on AI-assisted coding experience."""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def return_book(self):
        self.is_available = True
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            status = "Available" if book.is_available else "Not Available"
            print(f"Title: {book.title}, Author: {book.author}, Status: {status}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    print(f"You have borrowed '{title}'.")
                else:
                    print(f"'{title}' is currently not available.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                print(f"You have returned '{title}'.")
                return
        print(f"'{title}' not found in the library.")
# Example usage:
library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.display_books()
library.borrow_book("1984")
library.display_books()
library.return_book("1984")
library.display_books()
# Reflection on AI-assisted coding experience:
# The AI-generated code provided a solid foundation for the library management system.
# It effectively utilized classes, loops, and conditional statements to manage books.
# The structure was clear and easy to understand, making it straightforward to extend or modify.
# Overall, the experience was positive, and the AI assistance helped streamline the coding process.

"""Generate a Python class to mark and display student
attendance using loops.”
Expected Output:
• AI-generated attendance logic.
• Correct display of attendance.
• Test cases."""
class StudentAttendance:
    def __init__(self, student_name):
        self.student_name = student_name
        self.attendance_record = []

    def mark_attendance(self, day, is_present):
        self.attendance_record.append((day, is_present))

    def display_attendance(self):
        print(f"Attendance record for {self.student_name}:")
        for day, is_present in self.attendance_record:
            status = "Present" if is_present else "Absent"
            print(f"{day}: {status}")
# Example usage:
student = StudentAttendance("Alice")
student.mark_attendance("Monday", True)
student.mark_attendance("Tuesday", False)
student.mark_attendance("Wednesday", True)
student.display_attendance()

"""Generate a Python program using loops and conditionals
to simulate an ATM menu.”
Expected Output:
• AI-generated menu logic.
• Correct option handling.
• Output verification.
"""
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def display_menu(self):
        print("Welcome to the ATM!")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You have deposited: ${amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"You have withdrawn: ${amount}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Please select an option (1-4): ")
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter the amount to deposit: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter the amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
# Example usage:
atm = ATM(100)  # Initialize ATM with a balance of $100
atm.run()  # Start the ATM menu