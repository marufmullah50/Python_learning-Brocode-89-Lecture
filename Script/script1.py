'''''
# if _ _name__ = '_ _main__' : (this script can be imported or run standalone)


                             function and classes in this module can be 
                             reused
                             without the main block of code executing

    #example : Library = Import library for functionality when running library directly, display a help page                        
 # it's   just that you can run your library also import it by adding this if __name__ ='__main__':
    #         
    
    '''''
def fav_food(food):
    print(f"Your favorite food is {food}")
def main():
    print("This is script 1")
    fav_food("Rice")
    print("good bye!")


if __name__ ==  '__main__': # because of this even though script 2 import it doesn't work
    main()

