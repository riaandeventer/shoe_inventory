# Shoe Inventory Management Program

This Python program assists the clerk in the shoe store to keep track of the shoes in the store and for management to keep track of 
stock value and the need for restocking and running marketing campaigns.

## Description

This program reads from the text file inventory.txt and perform actions on the data, to prepare for presentation to managers.

We use a class named Shoes with the attributes: country, code, product, cost, and quantity.

Inside this class we define methods:
* get_cost - Returns the cost of the shoes.
* get_quantity - Returns the quantity of the shoes.
* str - Returns a string representation of a class.

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

The virtual environment requires the installation of python, pip & tabulate.

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

If your files copied successfully, there should be a folder shoe_inventory when you (for windows) enter the >dir command.
Go to this directory with below command.
```
>cd shoe_inventory
```
Now we can run the program with below command:
```
>python inventory.py
```

* The file inventory.txt contains the shoe data that you want to load initially. Update the information detail and note the format.
* The program will read in this file through a menu option and store the data in an object list.

### Executing Program

* Run the program
* You will see the menu.

![Main Menu](/images/menu.jpg)

* Menu Option 1: This will load the shoes from the inventory.txt file into the object list.
* Menu Option 2: This allows the user to add more shoe items.
* Menu Option 3: This allows the user to view all the shoe items in a table format.
* Menu Option 4: This allows the user to add more stock to items that are running low.
* Menu Option 5: Search for shoe with the code as input.
* Menu Option 6: Print the value of the shoes (number of shoes times the value of a shoe).
* Menu Option 7: Find shoe that is overstocked and put it up for sales promotion.
* Menu Option 8: Exit the program.

## Authors

Riaan Deventer  - [LinkedIn: @riaandeventer](https://www.linkedin.com/in/riaandeventer/)
