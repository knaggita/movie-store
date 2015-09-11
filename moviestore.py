# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 11:15:35 2015

@author: KEZIAH
"""
# used when calculating discount
import math
"""
clint module changes text color in python console.
In order to have agreat experience its better to run the code in python console

"""
from clint.textui import colored

# in all these classes init, intialises attributes of the class, its the class constructor
# define all movie attributes 
class Movie(object):
     # class constructor
    def __init__(self, name, category, price):
        self.name = name
        self.price = price
        self.category = category

# define a customer        
class Customer(object):
    # class constructor
    def __init__(self, name, idno,my_movies=[], fines=[], movies_returned=[]):
        self.my_movies= my_movies
        self.name = name
        self.idno = idno
        self.fines = fines
        self.movies_returned = movies_returned

# define a store keeper        
class Storekeeper(object):
     # class constructor
    def __init__(self, name, movies_lent=[],movies=[]):
        self.name=name
        self.movies_lent = movies_lent
        self.movies =movies
        
# define a loan 
class Loan(object):
     # class constructor
    def __init__(self, number_of_days):
        self.number_of_days = number_of_days
        
# method for entering movies
def enter_movie():
    validinput = 0   
    name = raw_input("Enter the movie name: ")
    print colored.green("\nChoose category\n1. new release @ 1000 per day\n2. Children's @ 300 per day\n3. Regular @ 500 per day" )           
    # validate user input
    while not validinput:
        try:
            categorychoice = int ( raw_input('Enter your choice [1-3] : '))            
            if categorychoice < 1 or categorychoice > 3 :
                print colored.red("Choice out of range. Try again")
            else:                       
                if categorychoice == 1:
                    # new release has a price of 1000 per day
                    category = "new release"
                    price = 1000
                elif categorychoice == 2:
                    # children's has a price of 300 per day
                    category = "Children's"
                    price = 300
                else:
                    # regular has aprice of 500 per day
                    category = "Regular"
                    price = 500
                movie = Movie(name, category, price)
                # Keziah is an instance of Storekeeper, add the movie to Storekeeper's movies                      
                Keziah.movies.append(movie)
                # help storekeeper know movie is well saved                                    
                print "Movie is saved"
                validinput = 1  ## set it to 1 to validate input and to terminate the while..not loop
        except ValueError :
            print colored.red("This is not an integer. Try again")

# method for entering new customers
def enter_customer():
    name=raw_input("Enter customer name: ")
    valid_id = 0
    # check input validity
    while not valid_id :
            try :
                    idno=int(raw_input("Enter customer id number: "))
                    if idno < 0 :
                         print colored.red(("Invalid number. Try again..."))
                    else:                    
                         valid_id = 1 ## set it to 1 to validate input and to terminate the while..not loop
            except ValueError :
                    print colored.red(("That is not an integer. Try again..."))            
    # instatiate Customer using the class constructor
    # create a new customer with input name and id                
    customer = Customer(name, idno)
    # help store keeper now the customer details added            
    customer_list.append(customer)    
    print "Customer registered."
    # for testing purposes only, print the customer name and id
    print [(y.name,y.idno) for y in customer_list]
    

# method for renting a movie
def rent_amovie():
    valid = 0
    # check input validity
    while not valid :
        try :
                idno=int(raw_input("Enter customer id number: "))
                if idno < 0 :
                     print colored.red(("Invalid number. Try again..."))
                else:                    
                     valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
        except ValueError :
                print colored.red(("That is not an integer. Try again..."))
                
    # loop through all the available customers            
    for customer in customer_list:
        if customer.idno == idno:
            movie_to_be_lent= raw_input("Enter the movie name: ")
            number_of_days = input("Enter number of days: ")
            for title in Keziah.movies:                       
                if title.name == movie_to_be_lent:
                    # instatiate loan using the defined class constructor                           
                    loan = Loan(number_of_days)
                    # create a dictionary having loan as key and movie title as value, add it to movies_lent
                    Keziah.movies_lent.append({loan:title})
                    # add moovie to customer movies
                    customer.my_movies.append(title)
                    # remove movie fromthe library
                    Keziah.movies.remove(title)
                    # for testing purpose, show the movies lent, the one added to customer's movies
                    print"Movies lent %s" % [b.name for b in customer.my_movies]
                
        else:
            print "Customer with id: {} does not exist. Try again....".format(idno)
                  
    print '\nName of customer:\t%s' %customer.name
    print 'Movies borrowed include'
    
    # display the the customer name, movie borrowed and respective prices
    print "-" * 95
    print colored.blue("%-15s  %-15s  %-15s %15s %15s" % ("Movie name", "Category", "Price @ day", "Number of days", "Total Price"))
    discount_calc = 0
    total_price = 0            
    for movie in customer.my_movies:
        total_price += (number_of_days*movie.price)
        if movie.category == "new release":
            discount_calc += 1
        print ("%-15s  %-15s  %-15d %15d %15d" % (movie.name, movie.category, movie.price, number_of_days, number_of_days*movie.price))
        
    print "-" * 95
    # calculate discount, if customer borrows more than one move in new release, they get 10% discount
    if discount_calc > 1:                              
        print "Discount: {}".format(math.ceil(total_price*0.1))
        print "Total price: {}".format(total_price - (total_price*0.1))
    elif discount_calc < 1 or discount_calc == 1:
        print colored.blue("Sorry dear, your discount is o")
        print colored.blue("Total price: {}".format(total_price))

# method for returning movies
def return_movie():
    valid = 0
    # check input validity
    while not valid :
        try :
                idno = int(raw_input("Enter customer id: "))
                movie_name = raw_input("Enter movie name of movie brought back: ")    
                num_of_days = int(raw_input("How many days did u stay with the movie: "))
                if idno < 0 or num_of_days < 0:
                     print ("Invalid number. Try again...")
                else:                    
                     valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
        except ValueError :
                print ("That is not an integer. Try again...") 
                
    # loop through customer list to see who is returning the movie
    for customer in customer_list:
        if customer.idno == idno:
            # loop through the loan movie dictionary to check for all the loan details
            for loan_movie_dictionary in Keziah.movies_lent:                       
                loan = loan_movie_dictionary.keys()[0]
               
                movie = loan_movie_dictionary.values()[0]
                number_of_days = loan.number_of_days
                
                print "-" * 50
                
                print colored.blue("%-15s  %-15s" % ("Movie name", "Number of days"))                                    
                print ("%-15s  %-15d" % (movie.name, number_of_days))
                if  num_of_days > number_of_days:
                    fine =  (num_of_days - number_of_days)*movie.price
                    print colored.blue("You have a fine of: {} shs".format(fine))
                else:
                    print colored.blue("You have no fine, thanks come again")
                    
                print "-" * 50 
                
                if movie.name == movie_name:
                    Keziah.movies.append(movie)
                   
                    Keziah.movies_lent.remove(loan_movie_dictionary)
                    customer.my_movies.remove(movie)
                    customer.movies_returned.append(movie)                             
                    print "Movies in the store %s" % Keziah.movies
                    print "Movies customer still has %s" % customer.my_movies
        else:
            print colored.red("Customer with id: {} does not exist. Try again....".format(idno))
            
# exit the program
def exit_program():
    pass


if __name__ == "__main__":
    
    # instatiate Storekeeper class using its constructor
    Keziah = Storekeeper("Keziah")
    # create alist of all the customers of the store
    customer_list=[]
    print colored.blue("******************** WELCOME TO MOVIE STORE*************************")
    while True:       
        
        print "-" * 50
        print colored.green("\nMAIN MENU \n1. Enter movie \n2. Enter customer \n3. Rent a movie\n4. Return movie \n5. Exit  ")
        print "-" * 50
        is_valid=0 
        while not is_valid :
                try :
                        choice = int ( raw_input('Enter your choice [1-5] : ') )
                        if choice < 1 or choice > 5:
                             print colored.red(("Invalid number. Try again..."))
                        else:                    
                             is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
                except ValueError :
                        print colored.red(("That is not an integer. Try again..."))
        
        if choice == 1:
            enter_movie()                    
        elif choice ==2:
            enter_customer()        
        elif choice == 3:
            rent_amovie() 
        elif choice == 4:
            return_movie()            
        else:
            print colored.blue("Exited successfully")            
            break
        



