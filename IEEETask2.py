import datetime
import os
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1203",
    database = "devam"
)
#os.getcwd()

class LMS:

    def __init__(self,list_of_books,library_name):
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),
            "lender_name": "","Issue_date":"","Status":"Available"}})
            Id = Id + 1

    def display_books(self):
        print("-----------------------------List Of Books-----------------------------")
        print("Books Id","\t","Title")
        print("-----------------------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"), "- [",value.get("Status"),"]")

    def Issue_books(self):
        books_id = input("Enter Book Id:")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} \
                 on {self.books_dict[books_id]['Issue_date']}")
                return self.Issue_books()
            elif self.books_dict[books_id]['Status'] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Issue_date'] = current_date
                self.books_dict[books_id]['Status'] = "Already Issued"
                print("Books Issued Successfully!!!!")
        else:
            print("Book Id not found!!!")
            return self.Issue_books()
    
    def add_books(self):
        new_books = input("Enter Book Title: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 75:
            print("Book Title is long, maximum 100 chars are allowed!!")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':"",
                'Issue_date':"",'Status':"Available"}})
                print(f"This book '{new_books}' has been added successfully!!!")

    def return_books(self):
        books_id = input("Enter Book Id: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print("This book is already available in the library. Please check your book Id.")
                return self.return_books()
            elif not self.books_dict[books_id]["Status"] == "Available":
                self.books_dict[books_id]["lender_name"] = ""
                self.books_dict[books_id]["Issue_date"] = ""
                self.books_dict[books_id]["Status"] = "Available"
                print("Successfully updated!!! \n")
        else:
            print("Book Id is not found")

    def search_by_title(self):
        btitle = input("Enter Book Title: ")
        sql = "SELECT * FROM books WHERE Title ='"+ btitle+"'"
        c = mydb.cursor()
        c.execute(sql)
        print(c.fetchall())

    def search_by_id(self):
        bid = input("Enter Book id: ")
        sql = "SELECT * FROM books WHERE Id ='"+ bid+"'"
        c = mydb.cursor()
        c.execute(sql)
        print(c.fetchall())

    def search_by_bc(self):
        bbc = input("Enter Book Barcode: ")
        sql = "SELECT * FROM books WHERE Barcode ='"+ bbc+"'"
        c = mydb.cursor()
        c.execute(sql)
        print(c.fetchall())

    def search_by_au(self):
        bau = input("Enter Book Author: ")
        sql = "SELECT * FROM books WHERE Author ='"+ bau+"'"
        c = mydb.cursor()
        c.execute(sql)
        print(c.fetchall())

    def search_by_cat(self):
        bcat = input("Enter Category: ")
        sql = "SELECT * FROM books WHERE Category ='"+ bcat+"'"
        c = mydb.cursor()
        c.execute(sql)
        print(c.fetchall())

    def search_by_py(self):
        bpy = input("Enter Book Publication year: ")
        sql = "SELECT * FROM books WHERE Pyear ='"+ bpy+"'"
        c = mydb.cursor()
        c.execute(sql)
        print(c.fetchall())

    def search_by_rack(self):
        brack = input("Enter Rack no.: ")
        sql = "SELECT * FROM books WHERE Rack ='"+ brack+"'"
        c = mydb.cursor()
        c.execute(sql)
        print(c.fetchall())

try:
    myLMS = LMS("List_of_books.txt","Python's Library")
    press_key_list = {"Z":"Search by Title","X":"Search by Id","Y":"Search by Barcode","F":"Search by Author",
    "G":"Search by Category","H":"Search by Publication Year","J":"Search by Rack No.","D": "Display Books",
    "I":"Issue Books","A":"Add Books","R":"Return Books","Q":"Quit"}
    key_press = " "
    while not (key_press == "q"):
        print(f"\n---------------- Welcome to {myLMS.library_name} Library Management System---------------- \n")
        for key, value in press_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press key: ").lower()
        if key_press == "i":
            print("\nCurrent Selection : Issue Book\n")
            myLMS.Issue_books()
        elif key_press == "a":
            print("\nCurrent Selection : Add Book\n")
            myLMS.add_books()
        elif key_press == "d":
            print("\nCurrent Selection : Display Books\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\nCurrent Selection : Return Book\n")
            myLMS.return_books()
        elif key_press == "z":
            myLMS.search_by_title()
        elif key_press == "x":
           myLMS.search_by_id()
        elif key_press == "y":
            myLMS.search_by_bc()
        elif key_press == "f":
            myLMS.search_by_au()
        elif key_press == "g":
            myLMS.search_by_cat()
        elif key_press == "h":
            myLMS.search_by_py()
        elif key_press == "j":
            myLMS.search_by_rack()
        elif key_press == "q":
            break
        else:
            continue
except Exception as e:
    print("Something went wrong kindly check your input!!!!!")
            
                
                
l = LMS("List_of_books.txt","Python's Library")
print(l.display_books())

        
    
        
        
    
    
    

    
    

   