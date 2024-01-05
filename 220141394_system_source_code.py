import random
from datetime import datetime, timedelta


# Define a class named Books
class Books:

    def __init__(self, title="", author="", year="", publisher="", num_copies=0, publication_date=""):
        """
               Construct a new Book object.

               Params: title: The title of the book
                       author: The author of the book
                       year: The year the book was published
                       publisher: The publisher of the book
                       num_copies: The number of available copies of the book
                       publication_date: The publication date of the book
               """
        self.book_id = random.randint(1, 10000)  # book_id is randomly generated and assigned to a book
        self.title = title.lower()  # Setting the title of the book
        self.author = author.lower()  # Setting the author of the book
        self.year = year  # Setting the year of the book
        self.publisher = publisher.lower()  # Setting the publisher of the book
        self.num_copies = num_copies  # Setting the total number  of the book copies
        self.available_copies = num_copies  # Setting the number of available copies,initially equal to total copies
        # Setting the publication date of the book
        self.publication_date = datetime.strptime(publication_date, "%Y-%m-%d").date() if publication_date else None

    # Define a function to set the book's title
    def set_title(self, title):
        """
                Set the title of the book.

                :parameter title: The new title of the book
                """
        self.title = title

    # Define a function to set the book's author
    def set_author(self, author):
        """
                Set the author of the book.

                :parameter author: The new author of the book
                """
        self.author = author

    # Define a function to set the book year
    def set_year(self, year):
        """
                Set the year the book was published.

                :parameter year: The publication year of the book
                """
        if not year.strip():
            print("Year cannot be empty.")
            self.year = None
        else:
            try:
                # Tries to convert the year input to an integer
                self.year = datetime.strptime(year, "%Y").year
            except ValueError:
                # Prints an error message if the year input is not a 4-digit number
                print("Invalid year format. Please enter a 4-digit year.")
                self.year = None

    # Define a function to set the publisher
    def set_publisher(self, publisher):
        """
                 Get the publisher of the book.
                 """
        self.publisher = publisher

    # Define a function to set number of copies of books
    def set_num_copies(self, num_copies):
        """
                 Get the number of copies of the book.
                 """
        try:
            # Try to convert the number of copies input to an integer
            self.num_copies = int(num_copies)
        except ValueError:
            print("Number of copies must be an integer")  # Displays a message for incorrect data input.
            self.num_copies = None

    # Define a function to set available copies of books
    def set_available_copies(self, available_copies):
        """
                 Sets available copies equal to total number of copies.
                 """
        self.available_copies = available_copies

    # Define a function to set the publication date
    def set_publication_date(self, publication_date):
        """
                  Get the publication date of the book.
                  """
        try:
            # Tries to convert publication date input to a date object
            self.publication_date = datetime.strptime(publication_date, "%Y-%m-%d").date() if publication_date else None
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD'.")  # Displays an error message for invalid date
            self.publication_date = None

    # Define a function to return the book's title
    def get_title(self):
        # Returns the title of the book
        return self.title.lower()

    # Define a function to return the book author
    def get_author(self):
        # Returns the author of the book
        return self.author.lower()

    # Define a function to return the book's year
    def get_year(self):
        # Returns the year of the book
        return self.year

    # Define a function to return the publisher
    def get_publisher(self):
        # Returns the publisher of the book
        return self.publisher.lower()

    # Define a function to return the number of copies of the book
    def get_num_copies(self):
        # Returns the total number of copies of the book
        return self.num_copies

    # Define a function to return the available copies
    def get_available_copies(self):
        # Returns the number of available copies of the book
        return self.available_copies

    # Define a function to return the publication date
    def get_publication_date(self):
        # Returns the publication date of the book
        return self.publication_date

    # Define a function that decreases the number of available books when borrowed
    def decrease_available_copies(self):
        # Decreases the number of available copies by 1 if there are any available copies left when borrowed
        if self.available_copies > 0:
            self.available_copies -= 1
        else:
            raise Exception("No copies available")

    # Define a function that increases the number of available books when returned.
    def increase_available_copies(self):
        # Increases the number of available copies by 1 when returned
        self.available_copies += 1

    # Define a function that gets the details from the user
    def get_details_from_user(self):
        # Gets details about the book from user input
        self.title = input("Enter book title: ").lower()
        self.author = input("Enter book author: ").lower()

        try:
            self.year = datetime.strptime(input("Enter book year: "), "%Y").year
        except ValueError:
            # Print a message when an error occurred.
            print("Invalid year format. Please enter a 4-digit year.")
            self.year = None

        self.publisher = input("Enter book publisher: ").lower()

        try:
            # Tries to convert the number of copies input to an integer
            self.num_copies = int(input("Enter number of copies: "))
            if self.num_copies <= 0:
                print("Number of copies cannot be negative or zero")  # Displays a notification for a number <= zero
                self.num_copies = None
        except ValueError:
            print("Number of copies must be an integer")  # Displays a message if input is not an integer
            self.num_copies = None

        self.available_copies = self.num_copies  # sets the available_copies to num_copies of books

        try:
            # Tries to convert publication date input to a date object
            self.publication_date = datetime.strptime(input("Enter publication date (YYYY-MM-DD): "), "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD'.")  # Displays an error message for wrong date format
            self.publication_date = None

    # Define a function to get book details
    def get_details(self):
        # Returns a dictionary containing all details about the book
        return {
            "Book ID": self.book_id,
            "Title": self.title.lower(),
            "Author": self.author.lower(),
            "Year": self.year,
            "Publisher": self.publisher.lower(),
            "Number of Copies": self.num_copies,
            "Available Copies": self.available_copies,
            "Publication Date": self.publication_date
        }


# Define a class named BookList
class BookList:
    # This is the constructor method that gets called when a new object is created .
    def __init__(self):
        # Initialize an empty dictionary to store books
        self.books = {}

    def add_book(self, book):
        # This method adds a book to the collection.
        # The book parameter is an instance of the Books class.
        self.books[book.book_id] = book

    # Define a function to edit book details
    def modify_book(self, title):
        """
        This method modifies a book in the collection.
        The title parameter specifies which book to modify.
        """
        try:
            # Get the book from the collection
            book = self.get_book_by_title(title.lower())

            if book is not None:
                while True:
                    # Ask the user which attribute they want to modify if the book exist
                    print("Which attribute do you want to modify?")
                    print("1. Title")
                    print("2. Author")
                    print("3. Year")
                    print("4. Publisher")
                    print("5. Number of copies")
                    print("6. Publication date")
                    print("7. Exit")

                    try:
                        choice = int(input("Enter the number of your choice: "))  # Ask the user what they want to edit
                    except ValueError:
                        # If the input is not a number, print an error message and continue the loop
                        print("Invalid input. Please enter a number.")
                        continue

                    if choice == 1:
                        # Choice 1 is for changing the title of the book
                        new_title = input("Enter the new title: ")
                        book.set_title(new_title)
                        print("The title has been updated.")

                    elif choice == 2:
                        # Choice 2 is for editing the author of the book
                        new_author = input("Enter the new author: ")
                        book.set_author(new_author)
                        print("The author has been updated.")

                    elif choice == 3:
                        # Choice 3 is for changing the year of the book
                        new_year = input("Enter the new year: ")
                        book.set_year(new_year)
                        print("The year has been updated.")

                    elif choice == 4:
                        # Choice 4 is for editing the publisher of the book
                        new_publisher = input("Enter the new publisher: ")
                        book.set_publisher(new_publisher)
                        print("The publisher has been updated.")

                    elif choice == 5:
                        # Choice 5 is for editing the total number of copies of the book
                        new_num_copies = input("Enter the new number of copies: ")
                        book.set_num_copies(new_num_copies)
                        print("The number of copies has been updated.")

                    elif choice == 6:
                        # Choice 6 is for editing the publication date of the book
                        new_publication_date = input("Enter the new publication date: ")
                        book.set_publication_date(new_publication_date)
                        print("The publication date has been updated. ")

                    elif choice == 7:
                        # Choice 7 is for exiting the editing book menu.
                        print("Exiting...")
                        break

                    else:
                        print("Invalid choice.")  # Displaying an invalid choice if the choice number is wrong

            else:
                print(f"No book found with title {title}")  # When the book is not found prints a notification message

        except Exception as e:
            # If an error occurs during execution, catch it and print an error message
            print(f"An error occurred: {str(e)}")

    # Define a function to display all the books in the  book collection
    def display_books(self):
        # This method prints all books in the collection by iterating through the dictionary of books
        for book_id, book in self.books.items():
            try:
                # Try to get the details of each book and print them
                book_details = book.get_details()
                print("Book ID:", book_id)
                print("Title:", book_details["Title"])
                print("Author:", book_details["Author"])
                print("Year:", book_details["Year"])
                print("Publisher:", book_details["Publisher"])
                print("Number of Copies:", book_details["Number of Copies"])
                print("Available Copies:", book_details["Available Copies"])
                print("Publication Date:", book_details["Publication Date"])
                print()
            except Exception as e:
                # If an error occurs during execution, catch it and print an error message
                print(f"An error occurred while displaying books: {str(e)}")

    # Define a function to search a book from the collection
    def search_book(self, search_by, search_query):
        """
               This method searches for a book in the collection by title, author, publisher or publication date.
               The search_by parameter specifies which attribute to search by.
               The search_query parameter specifies what value to search for.
               """
        try:
            found_books = []
            # Iterating over all books in the collection
            for book_id, book in self.books.items():
                # Checking if the search is by title
                if search_by.lower() == "title":
                    # If the search query is found in the book's title, add the book to the list
                    if search_query in book.title:
                        found_books.append(book)
                        # Checking if the search is by author
                elif search_by.lower() == "author":
                    # If the search query is found in the book's author, add the book to the list
                    if search_query in book.author:
                        found_books.append(book)
                        # Checking if the search is by publisher
                elif search_by.lower() == "publisher":
                    # If the search query is found in the book's publisher, add the book to the list
                    if search_query in book.publisher:
                        found_books.append(book)
                        # Checking if the search is by publication date
                elif search_by.lower() == "publication date":
                    # If the search query is found in the book's publication date, add the book to the list
                    if search_query in book.publication_date:
                        found_books.append(book)
                        # Returning all books that match the search query
            return found_books
        except Exception as e:
            # If an error occurs during execution, catch it and print an error message
            print(f"An error occurred while searching for books: {str(e)}")

    # Define a function to get a book by title
    def get_book_by_title(self, title):
        """
                This method finds a book in the collection using its title.
                The title parameter specifies which book to find.
                """
        try:
            # Iterating over all books in the collection
            for book_id, book in self.books.items():
                if book.title == title:
                    return book
            return None
        except Exception as e:
            # If an error occurs during execution, catch it and print an error message
            print(f"An error occurred: {str(e)}")

    # Define a function to remove a book from the book collection
    def remove_book(self, title):
        """
               This method removes a book from the collection using its title.
               The title parameter specifies which book to remove.
               """
        try:
            book_ids = []

            # Iterating over all books in the collection
            for book_id, book in self.books.items():
                # Checking if the title of the current book matches the given title
                if book.title == title:
                    # If a match is found, add the ID of the book to the list
                    book_ids.append(book_id)

            # Checking if no books were found with the given title
            if not book_ids:
                # If no books were found, print a message and return from the function
                print(f"The book '{title}' does not exist in the book collection.")
                return

            # Iterating over all found book IDs
            for book_id in book_ids:
                # Removing the book from the collection
                del self.books[book_id]
                # Printing a success message
                print(f"Successfully removed the book '{title}'.")

            return
        except Exception as e:
            # If an error occurs during execution, catch it and print an error message
            print(f"An error occurred: {str(e)}")

    def get_total_books(self):
        """
                This method returns the total number of books in the collection.
                """
        try:
            return len(self.books)
        except Exception as e:
            # If an error occurs , print an error message
            print(f"An error occurred: {str(e)}")


# Define a class called Users
class Users:
    # Define the initializer method for the class Users
    def __init__(self, username, firstname, surname, house_number, street_name, postcode, email, dob):
        # Initialize the user with the provided details
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email = email
        self.dob = dob

    # Define a function to return the user's username
    def get_username(self):
        return self.username

    def get_firstname(self):
        return self.firstname

    def get_surname(self):
        return self.surname

    def get_house_number(self):
        return self.house_number

    def get_street_name(self):
        return self.street_name

    def get_postcode(self):
        return self.postcode

    def get_email(self):
        return self.email

    def get_dob(self):
        return self.dob

    # Define a function to edit user's first name
    def edit_firstname(self, firstname):
        # Edit the first name of the user with error checking for empty string
        if firstname.strip() == "":
            print("First name cannot be empty.")
            return None
        else:
            self.firstname = firstname
            return self.firstname

    # Define a function to edit user's surname
    def edit_surname(self, surname):
        # Edit the surname of the user with error checking for empty string
        if surname.strip() == "":
            print("Surname cannot be empty.")
            return None
        else:
            self.surname = surname
            return self.surname

    # Define a function to edit the user's email
    def edit_email(self, email):
        # Edit the email of the user with error checking for valid email format
        if "@" not in email or "." not in email:
            print("Invalid email format.")
            return None
        else:
            self.email = email
            return self.email

    # Define a function to edit date of birth of the user
    def edit_dob(self, dob):
        # Edit the date of birth of the user with error checking for valid date format (YYYY-MM-DD)
        if len(dob.split("-")) != 3:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        else:
            self.dob = dob

    # Define a function to get user details
    def get_user_details(self):
        # Return a dictionary containing all details of the user
        return {
            "Username": self.username,
            "First Name": self.firstname,
            "Surname": self.surname,
            "House Number": self.house_number,
            "Street Name": self.street_name,
            "Postcode": self.postcode,
            "Email": self.email,
            "Date of Birth": self.dob
        }


# Define a class called UserList
class UserList:
    # Define the initializer method for the class UserList
    def __init__(self):
        # Initialize an empty dictionary to store users
        self.users = {}

    # Define a function to store users in a collection
    def store_user(self, user):
        # Store the user in the dictionary using their username as the key
        self.users[user.get_username()] = user

    # Define a function to display all users in users collection
    def display_users(self):
        # Display the details of all users
        for username, user in self.users.items():
            user_details = user.get_user_details()
            print("Username:", user_details["Username"])
            print("First Name:", user_details["First Name"])
            print("Surname:", user_details["Surname"])
            print("House Number:", user_details["House Number"])
            print("Street Name:", user_details["Street Name"])
            print("Postcode:", user_details["Postcode"])
            print("Email:", user_details["Email"])
            print("Date of Birth:", user_details["Date of Birth"])
            print()

    # Define a function to edit user's details
    def modify_user(self, username):
        # Get the user from the list
        user = self.get_user_by_username(username)
        if not user:
            # If no user is found with the given username, print an error message and return
            print(f"No user found with username {username}")
            return

        while True:
            if user is not None:
                # Ask the user which attribute they want to modify
                print("Which attribute do you want to modify?")
                print("1. Firstname")
                print("2. Surname")
                print("3. Email")
                print("4. Date of Birth")
                print("5. To exit")

                try:
                    choice = int(input("Enter the number of your choice: "))  # Ask the user what they want to edit
                except ValueError:
                    # If the input is not a number, print an error message and continue the loop
                    print("Invalid input. Please enter a number.")
                    continue

                if choice == 1:
                    # Choice 1 is to edit the first name of the user
                    new_firstname = input("Enter the new firstname: ").lower()
                    user.edit_firstname(new_firstname)
                    print("The firstname has been updated.")

                elif choice == 2:
                    # Choice 2 is to edit the surname of the user
                    new_surname = input("Enter the new surname: ").lower()
                    user.edit_surname(new_surname)
                    print("The surname has been updated.")

                elif choice == 3:
                    # Choice 3 is to edit the email of the user
                    while True:  # Keep asking for input until a valid email is entered
                        new_email = input("Enter the new email: ")
                        try:
                            user.edit_email(new_email)
                            print("The email has been updated.")
                            break  # If the email was successfully updated, break the loop
                        except ValueError:  # If an invalid email was entered
                            print("Invalid email format. Please enter a valid email.")

                elif choice == 4:
                    # Choice 4 is to edit the date of birth of the user
                    while True:  # Keep asking for input until a valid date of birth is entered
                        new_dob = input("Enter the new date of birth (YYYY-MM-DD): ")
                        try:
                            user.edit_dob(new_dob)
                            print("The date of birth has been updated.")
                            break  # If the date of birth is successfully updated, the loop breaks
                        except ValueError:  # If an invalid date of birth is entered
                            print("Invalid date format. Please enter a valid date in the format YYYY-MM-DD.")

                elif choice == 5:
                    # Choice 5 is to exit
                    print("Exiting...")
                    break  # If the user chooses to exit, the loop breaks
                else:
                    # Display a message of invalid choice if the choice is invalid or does not exist.
                    print("Invalid choice. Please enter a number between 1 and 5.")

    # Define a function to remove a user from the collection by firstname
    def remove_user(self, firstname):
        # Find all users with matching first name
        matching_users = [username for username, user in self.users.items() if
                          user.firstname.lower() == firstname.lower()]

        if len(matching_users) > 1:  # Checks if there is another user with the same first name
            print(
                f"There are multiple users with the name '{firstname}'. "
                f"Please provide more specific information to delete a user.")
            return  # Exit the function

        elif len(matching_users) == 1:  # Checks if there is only one user with that first name (Uniqueness)
            del self.users[matching_users[0]]
            print(f"Successfully removed the user '{firstname}'.")

        else:
            print(f"The user '{firstname}' does not exist in the dictionary.")

    # Define a function to count all users in the system
    def count_users(self):
        # Return the number of users in the dictionary
        return len(self.users)

    # Define a function to get user by entering the username
    def get_user_by_username(self, username):
        # Return the user with the given username if they exist, otherwise return None
        for user in self.users.values():
            if user.get_username() == username.lower():
                return user
        return None


# Define a class named Loans
class Loans:
    # Define the initializer method for the class Loans
    def __init__(self):
        # Initialize an empty dictionary to store users and their borrowed books
        self.loans = {}
        # Set the borrow date to 15 days ago
        self.borrow_date = datetime.now() - timedelta(days=15)

    # Define a function to get the return date of the borrowed book
    def get_return_date(self):
        # Calculate the return date based on the borrow date
        # If no borrow date is set, return None
        if self.borrow_date:
            return self.borrow_date + timedelta(days=14)
        else:
            return None

    # Define a function to borrow a book
    def borrow_book(self, list_of_users, list_of_books):
        try:
            # Ask for username and find the user in the users collection
            username = input("Enter your username: ").lower()

            user = list_of_users.get_user_by_username(username)
            # If user is not found, register a new user
            if user is None:
                print("User not registered. Registering now...")
                # Ask for registration details
                username = input("Enter your username: ").lower()  # User inputs username
                firstname = input("Enter your first name: ").lower()  # Input first name
                surname = input("Enter surname: ").lower()  # Input surname
                house_number = input("Enter house number: ")  # Input house number
                street_name = input("Enter street name: ")  # Input street name
                postcode = input("Enter postcode: ")  # Input postcode
                email = input("Enter email address: ")  # input email address
                dob = input("Enter date of birth (YYYY-MM-DD): ")  # Input date of birth

                # Create a new User instance and add it to the list of users
                user = Users(username, firstname, surname, house_number, street_name, postcode, email, dob)

                list_of_users.store_user(user)
                print(f"User {username} registered successfully!")  # Display a message of success registration

            # Ask for book title and find the book in the list of books
            book_title = input("Enter the title of the book you want to borrow: ").lower()
            book = list_of_books.get_book_by_title(book_title)

            # If book is not found or no available copies, prints a message
            if book is None:
                # If the book is not found in the book collection a message is displayed
                print("Book not found.")
                return

            if book.available_copies > 0:  # Check if the book is available
                # Add the book to the user's borrowed books and decrease available copies
                self.loans.setdefault(user, []).append(book)
                book.decrease_available_copies()
                print(f"You have successfully borrowed the book '{book.title}'.")
                return user, self.loans[user]  # return the user and their borrowed books
            else:
                # Display a message alerting that the chosen book is not available
                print(f"The book '{book.title}' is not available.")
        except Exception as e:
            # In case of , display an error message
            print(f"An error occurred: {e}")

    # Define a function to return books borrowed by a user
    def return_book(self, user, book):
        try:
            # Check if the user has borrowed any books
            if user in self.loans:
                # Check if the user has borrowed this specific book
                if book in self.loans[user]:
                    # Remove the book from the user's borrowed books and increase available copies
                    self.loans[user].remove(book)
                    book.increase_available_copies()
                    # Displaying a message of success return of book by title
                    print(f"You have successfully returned the book '{book.title}'.")
                else:
                    print(f"The book '{book.title}' is not borrowed by you.")
            else:
                # if user has no books borrowed print a message to show that the user did not borrow any books.
                print("You haven't borrowed any books.")
        except Exception as e:
            # If an error occurs, print an error message
            print(f"An error occurred: {e}")

    # Define a function to get total number of books borrowed by a user
    def get_total_borrowed_books(self, username):
        try:
            # Iterate over all users and their borrowed books
            for user, books in self.loans.items():
                # For the requested user, return their total number of borrowed books
                if user.username == username.lower():
                    return f"The user {username} is currently borrowing {len(books)} book(s)."
            return f"The user {username} is not currently borrowing any books."
        except Exception as e:
            # If an error occurs, print an error message
            print(f"An error occurred: {e}")

    # Define a function to print overdue books
    def print_overdue_books(self):
        try:
            # Get the current date
            today = datetime.today()
            # Iterate over all users and their borrowed books
            for user, books in self.loans.items():
                for book in books:
                    # Get the return date of the book
                    return_date = self.get_return_date()
                    # If a book is overdue , print its details along with the user's details
                    if return_date and return_date < today:
                        print(
                            f"Username: {user.get_username()}, First Name: {user.get_firstname()},"
                            f" Overdue Book: {book.title}")
                    else:
                        # If no book is overdue, print a notification message
                        print("No overdue book")
        except Exception as e:
            # If an error occurs, print an error message
            print(f"An error occurred: {e}")


def main():
    # Creating instances of the classes
    list_of_books = BookList()
    list_of_users = UserList()
    current_loans = Loans()
    new_book = Books()
    # Creating a list of books, where each book is represented as a dictionary
    books = [
        {
            "book_id": random.randint(1, 1000),  # randomly generated unique ID for the book
            "title": "Harry",  # Title of the book
            "author": "J.K. Rowling",  # Author of the book
            "year": "1997",  # Year of the book
            "publisher": "Bloomsbury Publishing",  # Publisher of the book
            "num_copies": 10,  # Number of copies of the book
            "publication_date": "1997-04-01"  # Publication date in YYYY-MM-DD format
        },
        {
            "book_id": random.randint(1, 1000),
            "title": "3 Little Hungry Girls",
            "author": "Eric Carley",
            "year": "2000",
            "publisher": "Unwind",
            "num_copies": 15,
            "publication_date": "2000-03-09"
        },
        {
            "book_id": random.randint(1, 1000),
            "title": "Green Birds",
            "author": "Dr.Seuss",
            "year": "2010",
            "publisher": "J.B. Lipoprotein & Co.",
            "num_copies": 4,
            "publication_date": "2010-07-11"
        },
        {
            "book_id": random.randint(1, 1000),
            "title": "1984",
            "author": "george orwell",
            "year": "2005",
            "publisher": "Sicker & Wartburg",
            "num_copies": 0,
            "publication_date": "2005-07-09"
        }
    ]

    # Create book objects from the dictionary and add them to the `BookList` using the `add_book` method
    # Iterating over each item in the books list
    for book_data in books:
        # Creating a Books object with the book data
        book = Books(
            title=book_data["title"],  # title of the book
            author=book_data["author"],  # author of the book
            year=book_data['year'],  # year of the book
            publisher=book_data["publisher"],  # publisher of the book
            num_copies=book_data["num_copies"],  # number of copies of the book
            publication_date=book_data["publication_date"]  # Publication date in YYYY-MM-DD format
        )
        # Adding the Books object to a collection
        list_of_books.add_book(book)

    # Creating a list of users, where each user is represented as a dictionary
    users = [
        {
            "username": "john1993",  # Username for the user
            "firstname": "john",  # Firstname for the user
            "surname": "joe",  # Surname for the user
            "house_number": "123",  # User's house number
            "street_name": "Main Street",  # User's street number
            "postcode": "263",  # User's postcode
            "email": "john@yahoo.com",  # User's email address
            "dob": "1990-01-01"  # Date of birth of the user in YYYY-MM-DD format
        },
        {
            "username": "sarah2000",
            "firstname": "sarah",
            "surname": "smith",
            "house_number": "001",
            "street_name": "First Avenue",
            "postcode": "4427",
            "email": "sarah@gmail.com",
            "dob": "1995-02-02"
        },
        {
            "username": "mary1991",
            "firstname": "mary",
            "surname": "bill",
            "house_number": "402",
            "street_name": "Third Boulevard",
            "postcode": "3402",
            "email": "mary@outlook.com",
            "dob": "1985-04-04"
        },
        {
            "username": "john74",
            "firstname": "john",
            "surname": "peter",
            "house_number": "664",
            "street_name": "Fourth Drive",
            "postcode": "789",
            "email": "john74@gmail.com",
            "dob": "1980-05-05"
        }
    ]

    # Creating a dictionary of users, where the key is the username and the value is the user data
    users_dict = {user['username']: user for user in users}

    # Iterating over each item in the dictionary
    for username, user_data in users_dict.items():
        # Creating a Users object with the user data
        user_data = Users(
            username=username,  # Username of the user
            firstname=user_data["firstname"],  # First name of the user
            surname=user_data["surname"],  # Surname of the user
            house_number=user_data["house_number"],  # User's house number
            street_name=user_data["street_name"],  # User's street name
            postcode=user_data["postcode"],  # User's postcode
            email=user_data["email"],  # User's email address
            dob=user_data["dob"]  # User's date of birth
        )
        list_of_users.store_user(user_data)

    # Infinite loop to keep the menu running until the user decides to exit
    while True:
        # Printing the options available in the library system menu
        print("\nLibrary System Menu:")
        print("1.  Add a book")  # Option to add a book
        print("2.  Search for a book")  # Option to search for a book
        print("3.  Remove a book")  # Option to remove a book
        print("4.  Add a user")  # Option to add a user
        print("5.  Remove a user")  # Option to remove a user
        print("6.  Borrow a book")  # Option to borrow a book
        print("7.  Return a book")  # Option to return a book
        print("8.  Count books currently borrowed by a user")  # Option to count books currently borrowed by a user
        print("9.  Print overdue books with user details")  # Option to print overdue books with user details
        print("10. Print user details")  # Option to print user details
        print("11. Print number of users in the system")  # Option to print number of users in the system
        print("12. View book collection")  # Option to view book collection
        print("13. Print number of books in the system")  # Option to print number of books in the system
        print("14. View users collection")  # Option to view users collection
        print("15. Modify book details")  # Option to modify book details
        print("16. Modify user details")  # Option to modify user details
        print("0.  Exit")  # Option to exit the system

        # Prompting the user to enter their choice from the menu options
        choice = input("Enter your choice (0-16): ")

        if choice == "1":
            # Create a new Book object and get details from the user
            new_book.get_details_from_user()

            # Add the book to the BookList
            list_of_books.add_book(new_book)

            # Print the book details
            print("Book added successfully:")
            book_details = new_book.get_details()
            for key, value in book_details.items():
                print(key + ":", value)

        elif choice == "2":
            # Search for a book

            search_by = input("Search by [title, author, publisher, publication date]: ").lower()
            search_query = input("Enter your search query: ").lower()
            found_books = list_of_books.search_book(search_by, search_query)

            # Display if the results of the book
            if found_books:
                print("Found Books:")
                for book in found_books:
                    book_details = book.get_details()
                    for key, value in book_details.items():
                        print(key + ":", value)
                    print()
            else:
                print("No books found with the specified search criteria.")

            # list_of_books.display_books()

        elif choice == "3":
            # Remove a book
            title = input("Enter the title of the book to remove: ").lower()
            list_of_books.remove_book(title)

        elif choice == "4":
            # Add a user
            user = Users('username', 'firstname', 'surname', 'house_number', 'street_name', 'postcode', 'email', 'dob')
            user.username = input("Enter username: ").lower()
            user.firstname = input("Enter first name: ").lower()
            user.surname = input("Enter surname: ").lower()
            user.house_number = input("Enter house number: ")
            user.street_name = input("Enter street name: ")
            user.postcode = input("Enter postcode: ")
            user.email = input("Enter email address: ")
            user.dob = input("Enter date of birth (YYYY-MM-DD): ")

            list_of_users.store_user(user)

            # Print the user details
            print("User added successfully:")
            user_details = user.get_user_details()
            for key, value in user_details.items():
                print(key + ":", value)

        elif choice == "5":
            # Remove a user
            firstname = input("Enter the first name of the user to remove: ").lower()
            list_of_users.remove_user(firstname)

        elif choice == "6":

            # Call the borrow_book method from the current_loans object
            current_loans.borrow_book(list_of_users, list_of_books)

        elif choice == "7":
            # Return a book
            username = input("Enter the username of the user returning the book: ")
            book_title = input("Enter the title of the book being returned: ")
            # Retrieve the User and Book objects based on the user input
            user = list_of_users.get_user_by_username(username)
            book = list_of_books.get_book_by_title(book_title)
            # Call the return_book method with the User and Book objects
            current_loans.return_book(user, book)

        elif choice == "8":
            # Count books currently borrowed by a user
            user = input("Enter the username of the user: ").lower()
            result = current_loans.get_total_borrowed_books(user)
            print(result)

        elif choice == "9":
            #  call print_overdue_books, it should print the overdue book
            current_loans.print_overdue_books()

        elif choice == '10':
            # print user details using username
            username = input("Enter the username of the user: ").lower()
            user = list_of_users.get_user_by_username(username)
            if user is not None:
                print(f"User details for {username}:")
                user_details = user.get_user_details()
                for key, value in user_details.items():
                    print(key + ":", value)
            else:
                print(f"No user found with username {username}")

        elif choice == '11':
            # printing the total number of users in the system
            total_users = list_of_users.count_users()
            print(f"Total number of users: {total_users}")

        elif choice == "12":
            # Print book collection
            list_of_books.display_books()

        elif choice == '13':
            # printing the total number of books in the system
            total_number_of_books = list_of_books.get_total_books()
            print(f"Total number of books: {total_number_of_books}")

        elif choice == "14":
            # Print user collection
            list_of_users.display_users()

        elif choice == "15":
            # Modify book details
            list_of_books.modify_book(input('Enter book title: ').lower())

        elif choice == "16":
            # Modify user details
            list_of_users.modify_user(input("Enter username: ").lower())

        elif choice == "0":
            # Exit the program
            print("Thank you for using the Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        while True:
            another_task = input("Do you want to perform another task? (yes/no): ")
            # Convert the input to lowercase to accept any case.
            another_task = another_task.lower()
            if another_task == 'yes':
                break
            elif another_task == 'no':
                print("Goodbye! Thank you for using the library.")
                exit(0)  # Exit the program
            else:
                # If the user enters anything other than 'yes' or 'no', ask again
                print("Invalid input. Please enter 'yes' or 'no'.")


# Checks  entry point to the program
if __name__ == "__main__":
    # Call main function
    main()
