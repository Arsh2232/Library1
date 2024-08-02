

flag=True #initializing a flag, used to break out of while loop

###creating 3 dictionries to store books###
#literature dictionary
dictLit={
    1:("Alice's Adventures in Wonderland","Lewis Carroll","06/27,2008"),
    2:("Moby Dick; Or, The Whale","Herman Melville","07/01/2001",),
    3:("Pride and Prejudice","Jane Austen","06/01/1998")
    }
#science dictionary
dictSci={
    4:("A Romance of Many Dimensions","Edwin Abbott Abbott","01/01/1994"),
    5:("Philosophiae Naturalis Principia Mathematica","Isaac Newton","03/01/2009"),
    6:("The Student's Elements of Geology","Sir Charles Lyell","02/01/2003")
    }
#natural history dictionary
dictNH={
    7:("Birds of the Rockies","Leander S. Keyser","07/05/2008"),
    8:("Handbook of the Trees of New England","Lorin Low Dame,Henry M. Brooks","01/28/2007")
    }

###creating a dictionary of tuples of all the shelves
dictShelves={"scibooks":(dictSci), "litbooks":(dictLit),"nathisbooks":(dictNH)}

###functions
def shelf(shelfName):#function to display the user's shelfname
    print("You are in {} shelf".format(shelfName))

def mainTwo():#function to go back to the main menu when user dosent want to read more
    askBack=input("Enter 'main' to go back to main menu: ").lower()
    if askBack=='main':
        main() 

def quitIt():#funciton to let the user exit the program
    global flag
    flag=False
    print("Visit again!\nBieee!")

def readFiles(filePath):#funciton that opens and reads files
    with open(filePath, encoding="utf-8") as myFile:
        index=0#first line
        till=25#last line
        lines=myFile.readlines()#returns a list 

        while index<len(lines):
            lastLine=lines[index:index+till]#initializes the 25th line as the next start line if user wants to continue
            for line in lastLine:
                print(line.strip())

            ask = input("Would you like to continue reading?\n yes or no: ")
            if ask =='yes':
                index+=till
            
            elif ask=='no':
                mainTwo()#nested function
                return

            if index+till>len(lines):#if the lines have ended, tells user the book has been read
                print("YOU HAVE REACHED THE END OF THE BOOK\nThank you for reading!")   
                
        
def scibooks():#funciton to access books in science dictionary
    for key,value in dictSci.items():#using .items() to return a view object  
        book,writer,date=value
        print("{}.{} \n   by {},\n   published on {}".format(key,book,writer,date))

def litbooks():#funciton to access books in literature dictionary
    for key,value in dictLit.items():
        book,writer,date=value
        print("{}.{} \n   by {},\n   published on {}".format(key,book,writer,date))

def nathisbooks():#funciton to access books in natural history dictionary
    for key,value in dictNH.items():
        book,writer,date=value
        print("{}.{} \n   by {},\n   published on {}".format(key,book,writer,date))

def main():
    while flag:#flag is true
        print("Welcome to the library\nEnter 'a' to go to literature shelf\nEnter 'b' to go to Science shelf\nEnter 'c' to go to natural history shelf\nEnter 'q' to quit ")
        askUser = input("Which self would you like to go to, Sci, Lit or Natural His? ")
       
        

        if askUser == 'a':
            shelf("Literature")#shelf function with literature as argument
            litbooks()#litbooks function to get access to lit. dictionary contents 
            askRead = int(input("which book would you like to read? \n Enter 1, 2, 3: "))
        #opening book using readfiles function according to the selected option
            
           
            if askRead == 1:
                readFiles("books/AliceInWonderland-L.txt")
            elif askRead ==2:
                readFiles("books/MobyDick-L.txt")                   
            elif askRead == 3:
                readFiles("books/PrideAndPrejudice-L.txt")
            else:
                print("Invalid entry, please read carefully")

        elif askUser == 'b':
            shelf("Science")
            scibooks()
            askRead = int(input("which book would you like to read? \n Enter 4, 5, 6: "))
 
            if askRead==4:
                readFiles("books/Flatland-S.txt")                   
            elif askRead==5:
                readFiles("books/PhilosophiaeNaturalisPrincipiaMathematica-S.txt")                   
            elif askRead==6:
                readFiles("books/TheStudentsElementsOfGeology-S.txt")
            else:
                print("Invalid entry, please read carefully")

        elif askUser =='c':
            shelf("natural history")
            nathisbooks()
            askRead = int(input("which book would you like to read? \n Enter 7, 8: "))
           
            if askRead==7:
                readFiles("books/BirdsOfTheRockies-NH.txt")                   
            elif askRead==8:
                readFiles("books/HandbookOfTheTreesOfNewEngland-NH.txt")
            
        elif askUser=='q':
            quitIt()

        else:
                print("Invalid entry, please read carefully")

###calling main funtion
main()


