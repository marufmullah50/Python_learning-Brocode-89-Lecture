'''''
# if _ _name__ = '_ _main__' : (this script can be imported or run standalone)


                             function and classes in this module can be 
                             reused
                             without the main block of code executing

    #example : Library = Import library for functionality when running library directly, display a help page
    # it's   just that you can run your library also import it by adding this if __name__ ='__main__':
    #                                                                            main()                                     
'''''
from script1 import *
def fav_drink(drink):
    print(f"your favourite drink is {drink}")
def main():
    print("This is Script 2")
    fav_food("Sushi")
    fav_drink("coffee")
    print("Good Bye")

if __name__ == '__main__':
    main()