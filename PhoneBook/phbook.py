import sqlite3

class PhBook:
    def __init__(self):
        self.conn = sqlite3.connect('test.db')
        self.cursor = self.conn.cursor() # Fixing it, so instead of creating it everytime, just using the existing one

        # Need to add more columns and then do changes in insert() function
        table = '''CREATE TABLE PhoneDIR (
        Name VARCHAR(255) NOT NULL,
        PHONE VARCHAR(255) NOT NULL
        );'''
        try:
            self.cursor.execute(table)
            print('A new PhoneBook is created, select what you want to do now!!!')
        except Exception as e:
            print(e)
        finally:
            self.display()

    # Simple CRUD display
    def display(self):
        while True:
            print('\n\nWelcome to your PhoneBook!!\n', '*'*75)
            print('\n1. Would you like to see the saved numbers?')
            print('\n2. Would you like to save a new number?')
            print('\n3. Would you like to delte a number?')
            print('\n4. Would you like to search a number?')
            print('\n5. Close the PhoneBook')
            choice = int(input('\nYou choice(1-5): '))

            if choice == 1:
                self.show()
            elif choice == 2:
                self.insert()
            elif choice == 3:
                self.delete()
            elif choice == 4:
                self.search()
            elif choice == 5:
                self.conn.close()
                print('\n------Closing the PhoneBook-----')
                break
            else:
                print('\nWRONG CHOICE!!!')
 
    # Displays all the record
    def show(self):
        try: #improving the exception cases
            self.cursor.execute('SELECT * FROM PhoneDIR')
            data = self.cursor.fetchall()
            print('Name', ' '*(30 - len('Name')) ,'||', 'Phone\n', '*'*50)
            for rows in data:
                print(rows[0], ' '*(30 - len(rows[0])) ,'||' , rows[1])
        except Exception as e:
            print(e)
        finally:
            print('These are all the records in your PhoneDIR')

    # Insert one element at a time
    def insert(self):
        print('\nFill the following fields!!\n')
        self.name = input('Name: ')
        self.phone = input('Phone: ')

        try:
            self.cursor.execute('INSERT INTO PhoneDIR VALUES (?, ?)', (self.name, self.phone,))
            self.conn.commit()
            print('Phone Number saved succesfully!!')
        except Exception as e:
            print(e)
        finally:
            choice = input('\nWanna save another?(Y/n): ')
            if choice == 'Y':
                self.insert()
            else:
                print('\n----Exiting Save mode-----')

    # Delete one item at a time    
    def delete(self):
        choice = input('\nDelete by Name(Y/n)?: ')
        try:
            if choice == 'Y':
                name = input('Enter the Contact Name: ')
                self.cursor.execute('DELETE FROM PhoneDIR WHERE Name = "%s"' % name)
            elif choice == 'n':
                number = input('Enter the Contact number: ')
                self.cursor.execute('DELETE FROM PhoneDIR WHERE Phone = "%s"' % number)
            self.conn.commit()
            print('\nDeleted successfully!!')
        except Exception as e:
            print(e)
        finally:
            choice = input('\nWanna delete another?(Y/n): ')
            if choice == 'Y':
                self.delete()
            else:
                print('\n----Exiting Delete mode-----')

    # Search by either name or phone number
    def search(self):
        choice = input('\nSearch by Name(Y/n)?: ')
        try:
            if choice == 'Y':
                name = input('Enter the contact name: ')
                self.cursor.execute('SELECT * FROM PhoneDIR WHERE Name = "%s"' % name)
            elif choice == 'n':
                number = input('Enter the contact number: ')
                self.cursor.execute('SELECT * FROM PhoneDIR WHERE Phone = "%s"' % number)
            data = self.cursor.fetchall()
            print('Name', ' '*(30 - len('Name')) ,'||', 'Phone\n', '*'*20)
            for rows in data:
                print(rows[0], ' '*(30 - len(rows[0])) ,'||' , rows[1])
        except Exception as e:
            print(e)
        finally:
            print('These are all the records in your PhoneDIR')
        

if __name__ == '__main__':
    obj = PhBook()