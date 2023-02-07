# Software Engineer: RIAAN VAN DEVENTER (SN: RV22110005417)
# This was programmed for the Software Engineering BOOTCAMP
# Written on 27 December 2022

# ************** L1T30 - TASK ASSIGNMENT **************  
#
# Code a Python program that will read from the text file inventory.txt and
# perform the following on the data, to prepare for presentation to your managers:
# Create a class named Shoes with the following attributes:
# country, code, product, cost, and quantity.
# 
# Inside this class define the following methods:
#   ▪ get_cost - Returns the cost of the shoes.
#   ▪ get_quantity - Returns the quantity of the shoes.
#   ▪ __str__ - This method returns a string representation of a class.
#
# Outside this class create a variable with an empty list. 
# This variable will be used to store a list of shoes objects
#
# Define the following functions outside the class:
#   ▪ read_shoes_data - This function will open the file inventory.txt and 
#     read the data from this file, then create a shoes object with this data and 
#     append this object into the shoes list. 
#     One line in this file represents data to create one object of shoes. 
#     You must use the try-except in this function for error handling. 
#     Remember to skip the first line using your code.

#   ▪ capture_shoes - This function will allow a user to capture data about 
#     a shoe and use this data to create a shoe object and append this object inside the shoe list.

#   ▪ view_all - This function will iterate over the shoes list and print the details of the shoes returned from 
#     the __str__ function. 
#     Optional: you can organise your data in a table format by using Python’s tabulate module.
#   ▪ re_stock - This function will find the shoe object with the lowest quantity, which is the shoes that need to be
#     re-stocked. Ask the user if they want to add this quantity of shoes and then update it. 
#     This quantity should be updated on the file for this shoe.
#   ▪ search_shoe - This function will search for a shoe from the list
#     using the shoe code and return this object so that it will be printed.
#   ▪ value_per_item - This function will calculate the total value for each item. 
#     Please keep the formula for value in mind; value = cost * quantity. 
#     Print this information on the console for all the shoes.
#   ▪ highest_qty - Write code to determine the product with the
#     highest quantity and print this shoe as being for sale.
#   
# o Now in your main create a menu that executes each function above. 
#   This menu should be inside the while loop. Be creative!
#
# ****************************************************** 
#   Import Libraries
# ******************************************************

# At first I received an error that the tabulate module does not exist.
# In my command prompt with administrator rights and path as below, I entered 
# path c:\Windows\system32>py -m pip install tabulate
# to install the module. Available for Python 3.7+ only.
# Had to remove tabulate for docker implementation
# from tabulate import tabulate

# ****************************************************** 
#   Create Class Definitions
# ******************************************************
# Create a base class called Shoe.
class Shoes:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)
        
    def get_cost(self):
        '''
        Write code to return the cost of the shoe in this method.
        '''
        return (self.cost)

    def get_quantity(self):
        '''
        Write code to return the quantity of the shoes.
        '''
        return (self.quantity)

    def __str__(self):
        '''
        Write code to return a string representation of a class.
        This method can be used to display data. 
        '''
        return (f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}")

#=============Shoe list===========

# The list will be used to store a list of objects of shoes.
shoes_lst = []
#========== Functions outside the class ==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt and read the data from this file, 
    then create a shoes object with this data and append this object into the shoes list. 
    One line in this file represents data to create one object of shoes. 
    Used the try-except in this function for error handling. 
    Remembered to skip the first line headings using the code.
    '''
    # If we find the inventory.txt file then f_invent will change from None to a representation of the file.
    f_invent = None
    # If the file is empty then file_reads_bln will be changed to False.
    file_reads_bln = True
        
    while f_invent == None :
        
        try:
            # Open the file for read mode. If the file is found then f_invent value will change and 
            # the while f_invent == None will not repeat at the end of this instance.
            f_invent = open ("./inventory.txt", "r")
           
            # Read the first line of headings as to not include it in the shoe list.
            # For an empty file we are using next() to catch an except StopIteration.
            next(f_invent)

            # Now read through the rest of the file from line 2 till end.
            for line in f_invent :
                if line.strip () :
                    # We remove the next line character to fix the data value at the end of the line.
                    line = line.replace ("\n", "")
                    # Separate the string by "," and place the parts into a list.
                    new_shoes_lst = line.split (",")
                    # Declare the class Shoes variable with the values in new_shoes_lst and append it to the shoes_lst.
                    shoes_cls = Shoes (new_shoes_lst [0], new_shoes_lst [1], new_shoes_lst [2], new_shoes_lst [3], new_shoes_lst [4])
                    shoes_lst.append (shoes_cls)

        # If the file in the open statement above is not found then this FileNotFoundError logic will run.
        except FileNotFoundError:
            print ()
            print("--> The inventory file cannot be found in the folder.")

        # If the file exists but has no data in it, then we will get this error on the next(f_invent) statement.
        except StopIteration:
            file_reads_bln = False
            print ()
            print("--> The inventory file is empty.")
        
        finally:
            # If the file is not found, we will get an error on f_invent.close (), so we will only execute
            # this if we found the file represented by f_invent value changing from None.
            if f_invent is not None:
                f_invent.close()
            # If we had a successful first read and if there were shoes inventory entries, then we will
            # display success message else we will display error message.
            if file_reads_bln == True and len (shoes_lst) > 0:
                print ()
                print ("--> Shoes inventory loaded.")
            else :
                print ()
                print ("--> Shoes inventory load error... CHECK the Inventory File content!")
                    
def capture_shoes():
    '''
    This function will allow a user to capture (input) data about a shoe and use this data to create a shoe object
    and append this object inside (to) the shoe list.
    Note: There is no request to update the file with this capture. Same logic as re-stock quantity 
          update can be implemented here to update the file, however if re_stock is
          run after capture_shoes then all the items, including the captures in shoes_lst 
          will be written to file.
    '''
    # Make sure that the shoes_lst has been loaded as to not capture duplicates.
    if len (shoes_lst) == 0 :
        read_shoes_data()

    print ()
    cap_country_str = input ("Enter country : ")

    # Keep capturing the code until it is a unique value.
    while True :
        cap_code_str = input ("Enter code : ").upper ()

        code_dupl_bln = False

        for i in range (len (shoes_lst)) :
            if shoes_lst [i].code == cap_code_str :
                code_dupl_bln = True
                print ()
                print ("--> That code is already logged. Please try a different code...")
                break   # Exit for i in range loop
    
        if code_dupl_bln == False :
            break   # Exit While True loop

    cap_product_str = input ("Enter product name : ")

    # Keep capturing cost until the value is valid.
    while True :
        try : 
            cap_cost_int = int (input ("Enter cost : "))
            if cap_cost_int > 0 :
                break
            else :
                print ()
                print ("--> That was not a valid input. Please try again ...")

        # Display message if cost capture is not an integer.
        except ValueError :
            print ()
            print ("--> That was not a valid input. Please try again ...")
    
    # Keep capturing quantity until the value is valid.
    while True :
        try : 
            cap_quant_int = int (input ("Enter stock quantity : "))
            if cap_cost_int > 0 :
                break
            else :
                print ()
                print ("--> That was not a valid input. Please try again ...")

        # Display message if quantity capture is not an integer.
        except ValueError :
            print ()
            print ("--> That was not a valid input. Please try again ...")

    # Now that we have all the values, use the shoes class to store all the values and append it to the shoes_lst.
    shoes_cls = Shoes (cap_country_str, cap_code_str, cap_product_str, cap_cost_int, cap_quant_int)
    shoes_lst.append (shoes_cls)

    print ()
    print ("--> Shoes inventory item was added.")

def view_all():
    '''
    This function will iterate over the shoes list and use the details of the shoes returned from 
    the __str__ function to build the data table for the Python's tabulate module that will display the inventory.
    '''
    # Make sure that the shoes_lst has been loaded.
    if len (shoes_lst) == 0 :
        read_shoes_data()
    
    # If the shoes_lst is still empty then the Inventory.txt file is empty 
    # and is dealt with inside read_shoes_data().
    if len (shoes_lst) > 0 :
        # table_nlst is a nested list with headings as the first entry.
        table_nlst = [["Country", "Code", "Product", "Cost", "Quantity"]]
        print()
        print ("======================== Shoes Inventory ========================\n")
        print ("Country      | Code        | Product       | Cost         | Quantity\n") # Added for tabulate removal

        # Move the list of objects into a list of lists.
        for i in range (len (shoes_lst)) :
            table_row_lst = shoes_lst [i].__str__().split (", ")
            table_nlst.append (table_row_lst)
            print(table_row_lst) # Added for tabulate removal

        # Use tabulate imported module to display the data in table format.
        #   print ()
        #   print ("======================== Shoes Inventory ========================\n")
        #   print (tabulate(table_nlst, headers = 'firstrow')) 
        print ("=================================================================")

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoe that needs to be re-stocked. Ask the user if they
    want to add a quantity of shoes and then update it in the shoes_lst
    and the inventory file for this shoes.
    '''
    # Make sure that the shoes_lst has been loaded.
    if len (shoes_lst) == 0 :
        read_shoes_data()

    # No specifications were provided for when 2 instances are equally the lowest, 
    # so we will assume that the lowest is unique.
    # If there were multiple equal instances, we could just append it to our list for multiple instances
    # or the user can just run re_stock () multiple times to get the new lowest after previous has been updated.

    # If the shoes_lst is still empty then the Inventory.txt file is empty 
    # and is dealt with inside read_shoes_data().
    if len (shoes_lst) > 0 :
        
        for i in range (len (shoes_lst)) :
            # Start with a benchmark and move the first shoes into lowest_quant_lst.
            # For all the other instances, store shoes if it is lower than the current quantity value.
            if i == 0 or shoes_lst [i].quantity < lowest_quant_cls.quantity :
                lowest_quant_cls = shoes_lst [i]
                # Store the index of the lowest quantity record so we can come back for the update.
                lowest_quant_idx = i

        # Tabulate table contains the list of attributes for the lowest quantity shoes.
        ttable_lst = [lowest_quant_cls.__str__().split(", ")]
        
        print ()
        print ("================= Lowest Quantity Shoes Inventory =================\n")
        #   print (tabulate(ttable_lst, headers = ["Country", "Code", "Product", "Cost", "Quantity"]))
        print ("Country      | Code        | Product       | Cost         | Quantity\n")
        print (ttable_lst)
        print ("===================================================================\n")

        shoes_stock_chr = input ("Would you like to add stock to the inventory? Answer (Y)es or (N)o > ").lower ()
        # If choice is blank, set it to space to avoid error in below if == "y" statement.
        if shoes_stock_chr == "" :
            shoes_stock_chr = " "
    
        # If the choice is yes then request stock number.
        if shoes_stock_chr [0] == "y" :
            # Use try-except to make sure the stock number is an integer value.
            while True :
                try : 
                    print ()
                    shoes_stock_int = int (input ("How many shoes would you like to add to this stock? > "))
                    # Update the shoes_lst.
                    shoes_lst [lowest_quant_idx].quantity = shoes_lst [lowest_quant_idx].quantity + shoes_stock_int
                
                    # Overwrite inventory.txt with updated shoes_lst.
                    # If the inventory.txt file does not exist, it will be created.
                        
                    # Open the inventory.txt file for write mode.
                    f_invent = open ("./inventory.txt", "w")

                    # Write the header line.
                    f_invent.write ("Country,Code,Product,Cost,Quantity\n")

                    # Write the updated shoes_lst to file.
                    for i in range (len(shoes_lst)) :
                        line_str = shoes_lst [i].__str__ ()
                        # Remove the spaces after the commas and add the next line character at the end.
                        line_str = line_str.replace (", ", ",") + "\n"
                        f_invent.write (line_str)
                
                    f_invent.close()

                    print ()
                    print ("--> Shoes inventory updated.")

                    # Exit while True : loop
                    break 

                except ValueError :
                    print ()
                    print ("--> That was not a valid input. Please try again ...")

        elif shoes_stock_chr [0] == "n" :
            print ()
            print ("--> You chose not to add stock. Back to menu...")
        else : 
            print ()
            print ("--> Invalid input. Back to menu...")

def search_shoe():
    '''
     This function will search for a shoe from the shoes_lst
     using the shoe code and return this object for printing.
    '''
    # Make sure that the shoes_lst has been loaded else there is no list to search.
    if len (shoes_lst) == 0 :
        read_shoes_data()

    # If the shoes_lst is still empty then the inventory.txt file is empty and dealt with
    # inside read_shoes_data ()
    if len (shoes_lst) > 0 :
        print ()
        # Accept uppercase code to avoid incorrect comparison errors.
        srch_code_str = input ("Enter code : ").upper ()

        # Set a boolean to use as a find flag.
        code_find_bln = False

        for i in range (len (shoes_lst)) :
            if shoes_lst [i].code == srch_code_str :
                # srch_table_lst contains the list of attributes for the searched code.
                srch_table_lst = [shoes_lst [i].__str__().split(", ")]
                # Set the flag that the search was successful.
                code_find_bln = True
                # Exit the for loop since we found our code and need not search any further.
                break
        
        # Now we test for our successful find in case we completed the above loop range and 
        # never entered the if statement of the for loop.
        if code_find_bln == True :
            print ()
            print ("================== Shoes Inventory Search Result ==================\n")
            print ("Country      | Code        | Product       | Cost         | Quantity\n")
            print (srch_table_lst)
            #   print (tabulate(srch_table_lst, headers = ["Country", "Code", "Product", "Cost", "Quantity"]))
            print ("===================================================================")
        else :
            print ()
            print ("--> Code not found. Back to menu...")

def value_per_item():
    '''
    This function calculates the total value for each item.
    The formula for value : value = cost * quantity.
    We print this information on the console for all the shoes.
    '''
    # Make sure that the shoes_lst has been loaded.
    if len (shoes_lst) == 0 :
        read_shoes_data()
    
    # If the shoes_lst is still empty then the Inventory.txt file is empty 
    # and dealt with inside read_shoes_data ()
    if len (shoes_lst) > 0 :
        # val_table_nlst is a nested list with first instance being the headers for our table.
        val_table_nlst = [["Country", "Code", "Product", "Cost", "Quantity", "Total Value"]]
        print()
        print ("======================== Shoes Inventory - Total Value ========================\n")
        print ("Country    | Code      | Product       | Cost    | Quantity    | Total Value")
        #   print (val_table_nlst[0])
        print()

        for i in range (len (shoes_lst)) :
            # Calculate the total value for this instance.
            total_value_int = shoes_lst [i].get_cost () * shoes_lst [i].get_quantity ()
            # Use the __str__ method for the string representation of the instance and add a seperator 
            # and the string format of the total_value_int to the end of the string, then we split 
            # the items into a list by using the ", " separator.
            table_row_lst = (shoes_lst [i].__str__() + ", " + str(total_value_int)).split (", ")
            # Add this instance to our table for our display.
            val_table_nlst.append (table_row_lst)
            print (table_row_lst)

        #   print ()
        #   print ("======================== Shoes Inventory - Total Value ========================\n")
        #   print (tabulate(val_table_nlst, headers = 'firstrow'))
        print ("===============================================================================")

def highest_qty():
    '''
    Find the product with the highest quantity and print this shoe as being for sale.
    '''
    # Make sure that the shoes_lst has been loaded.
    if len (shoes_lst) == 0 :
        read_shoes_data()

    # If the shoes_lst is still empty then the Inventory.txt file is empty 
    # and dealt with inside read_shoes_data ().
    if len (shoes_lst) > 0 :
        
        for i in range (len (shoes_lst)) :
            # Start with a benchmark and move the first shoes into highest_quant_lst.
            # For all the other instances, store shoes if it is higher than the current quantity value.
            # Even though highest_quant_cls is referenced below before it is defined, i == 0 will run first and 
            # define and set a value for highest_quant_cls before the 'or shoes_lst [i].quantity > highest_quant_cls.quantity'
            # is reference in the 2nd instance of the 'for i in range' loop and will therefor not produce a runtime error.
            if i == 0 or shoes_lst [i].quantity > highest_quant_cls.quantity :
                highest_quant_cls = shoes_lst [i]
        # Tabulate table contains the list of attributes for the lowest quantity shoes.
        ttable_lst = [highest_quant_cls.__str__().split(", ")]
        
        print ()
        print ("================= Highest Quantity Shoes Inventory =================\n")
        print ("Country      | Code        | Product       | Cost         | Quantity\n")
        print (ttable_lst)
        #   print (tabulate(ttable_lst, headers = ["Country", "Code", "Product", "Cost", "Quantity"]))
        print ("===================================================================\n")
        print ("*******************************************************************")
        print (f"\t{highest_quant_cls.product} is FOR SALE at 25% discount!")
        print ("*******************************************************************")

# ============  MAIN LOGIC - Inventory Management  ===============

#========== Main Menu =============
# Create a menu that executes each function above.
menu_int = 0

while menu_int != 8 :
    # Display inventory menu until valid option is chosen.
    while True :
        try : 
            print ()
            print ("============ Inventory MENU ================")
            print ("1. Read Shoes Data")
            print ("2. Capture Shoes")
            print ("3. View All")
            print ("4. Re-Stock")
            print ("5. Search Shoe with Code")
            print ("6. Print values of shoes")
            print ("7. Find higest quantity for sales promotion")
            print ("8. Exit Program")
            print ("=============================================\n")

            menu_int = int (input ("Please choose a menu option (e.g. 1 to 8) > "))

            if menu_int > 0 and menu_int < 9 :
                break
            else :
                print ()
                print ("--> That was not a valid option. Please try again ...")
    
        except ValueError :
            print ()
            print ("--> That was not a valid option. Please try again ...")

#========== Options Logic =============    
    if menu_int == 1 :

        # Set shoes_load choice to yes to load if data has not already loaded,
        # since it won't enter the below if to ask if load is needed.
        shoes_load_chr = "y"

        # If data has already loaded, request if a reload is needed.
        if len (shoes_lst) > 0 :
            print ()
            print ("--> The shoes inventory has already been loaded!\n")
            shoes_load_chr = input ("Would you like to reload the inventory? Answer (Y)es or (N)o > ").lower ()
            # If choice is blank, set it to space to avoid error in below if == "y" statement.
            if shoes_load_chr == "" :
                shoes_load_chr = " "
    
        # If the choice is yes then load data.
        if shoes_load_chr [0] == "y" :
            shoes_lst.clear ()
            read_shoes_data()

        elif shoes_load_chr [0] == "n" :
            pass
        else : 
            print ()
            print ("--> Invalid input.")

    elif menu_int == 2 :
        capture_shoes()

    elif menu_int == 3 :
        view_all()

    elif menu_int == 4 :
        re_stock()

    elif menu_int == 5 :
        search_shoe()

    elif menu_int == 6 :
        value_per_item()

    elif menu_int == 7 :
        highest_qty()

    elif menu_int == 8 :
        print ()
        print ("Goodbye!\n")

# =================  END PROGRAM LOGIC HERE  ====================