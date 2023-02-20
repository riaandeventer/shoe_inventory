# Shoe Inventory Management Program

This Python program helps the clerk in the shoe store to keep track of the shoes in the store and for management

## Description

This program reads from the text file inventory.txt and perform actions on the data, to prepare for presentation to managers.

We use a class named Shoes with the attributes: country, code, product, cost, and quantity.

Inside this class we define methods:
* get_cost - Returns the cost of the shoes.
* get_quantity - Returns the quantity of the shoes.
* __str__ - Returns a string representation of a class.

Outside the class we create a variable with an empty list to store a list of shoes objects.

We also defined the following functions outside the class:

* read_shoes_data - This function opens the file inventory.txt and read the data from this file, 
      then we create a shoes object with this data and append this object into the shoes list. 
      One line in this file represents data to create one object of shoes. 
      We use the try-except in this function for error handling. 

* capture_shoes - This function will allow a user to capture data about additional shoes and use this data to 
      create a shoe object and append this object inside the shoe list.

* view_all - This function will iterate over the shoes list and print the details of the shoes returned from the __str__ function. 
      We organise the data in a table format by using Python’s tabulate module.
      
* re_stock - This function will find the shoe object with the lowest quantity, which is the shoes that need to be re-stocked. 
      We ask the user if they want to add this quantity of shoes and then update it. 
      The quantity is also updated on the file for this shoe.

* search_shoe - This function searches for a shoe from the list using the shoe code and return this object so that it will be printed.

* value_per_item - This function calculates the total value for each item. 
      The information is printed on the console for all the shoes.
      
* highest_qty - This code to determines the product with the highest quantity and print this shoe as being for sale.

## Table of Content
1. Installation
2. Executing Program
3. Authors

### Dependencies

* This program uses the tabulate function.

### Installation

### 1.  Implementing the program in a virtual environment.

##### 1.1   Dependencies

The virtual environment requires the installation of python & tabulate.

To install tabulate:

In command prompt with administrator rights and path as below, enter
path c:\Windows\system32>py -m pip install tabulate

--> Available for Python 3.7+ only.

##### 1.2   Copying Files

Go to the directory or folder where you want to install the project and enter the following command in the command line:
```
>git clone https://github.com/riaandeventer/shoe_inventory
```
If you are asked for a login then it should be because you might have made a typing error with the link.

##### 1.3   Run Program

If your files copied successfully, there should be a folder ebook_store when you (for windows) enter the >dir command.
Go to this directory with below command.
```
>cd shoe_inventory
```
Now we can run the program with below command:
```
>python inventory.py
```

* The file InventoryReset.txt contains the book data that you want to load initially. Update the information detail and note the format.
* The program will read in this file through a menu option and the database with table will be created or updated if it already exists.
* After initial load, you will notice the database file ebookstore_db in the folder.
* Database is called ebookstore and a table called books. The table has the following structure:

|Id     | Title                                     | Author             | Qty  |
|-------|-------------------------------------------|--------------------|------|
|3001   | A Tale of Two Cities                      | Charles Dickens    | 30   |
|3002   | Harry Potter and the Philosopher's Stone  | J.K. Rowling       | 40   |
|3003   | The Lion, the Witch and the Wardrobe      | C. S. Lewis        | 25   |
|3004   | The Lord of the Rings                     | J.R.R Tolkien      | 37   |
|3005   | Alice in Wonderland                       | Lewis Carroll      | 12   |

### Executing Program

* Run the program
* You will see the menu.

![Main Menu](/images/1.jpg)

* Menu Option 6: Start here to load the database or reset it in the future.
* Menu Option 1: This will straight display all the books in the inventory.
* Menu Option 2: This will request an identification number for the book, then book title, author and quantity you have available.
* Menu Option 3: You need the id of a book to update the title, author or quantity available. Use Menu Option 1 to get id number.
* Menu Option 4: Remove a book from you inventory by providing the id of the book. Use Menu Option 1 to get the id number.
* Menu Option 5: Search for books with below menu.

![Main Menu](/images/2.jpg)

* Menu Option 5: With submenu option 4 you can search for books with stock less than a certain number.

## Authors

Riaan Deventer  - [LinkedIn: @riaandeventer](https://www.linkedin.com/in/riaandeventer/)
