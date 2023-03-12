import xmlrpc.client
import sys

## Initialize connection to the server
s = xmlrpc.client.ServerProxy('http://localhost:8000')

## While loop when the loop = 1
loop = 1

while (loop == 1):
    ## Interface
    print("Select Option:")
    print("1: Search topic")
    print("2: Add topic")
    print("3: Exit")
    selectInput = input('\nEnter option: ')
    print()

    ## Check input
    ## Search topic
    if (selectInput == "1"):
        topicInput = input('Enter topic to search: ')
        print()

        ## Call print function
        try:
            result = s.print(topicInput)
            if (result == ""):
                print("Topic was not found!")
            else:
                print(result)

        ## No connection for example not running server.py
        except ConnectionRefusedError as err1:
            sys.exit("Connection error")
        
        ## Built in xmlrpc fault errors
        except xmlrpc.client.Fault as err2:
            print("A fault occurred")
            print("Fault code: %d" % err2.faultCode)
            print("Fault string: %s" % err2.faultString)

    ## Add topic
    elif (selectInput == "2"):
        ## Gather inputs
        titleInput = input("Enter title: ")
        noteInput = input("Enter note: ")
        textInput = input("Enter text: ")

        ## Call add function
        try:
            result = s.add(titleInput, noteInput, textInput)
            
            if (result == "Failure"):
                print("Topic was not added succesfully!\n")
            else:
                print("Topic was added succesfully!\n")
        
        ## No connection for example not running server.py
        except ConnectionRefusedError as err1:
            sys.exit("Connection error")
        
        ## Built in xmlrpc fault errors
        except xmlrpc.client.Fault as err2:
            print("A fault occurred")
            print("Fault code: %d" % err2.faultCode)
            print("Fault string: %s" % err2.faultString)
    
    ## Exit program
    elif (selectInput == "3"):
        print("Exiting program\n")
        loop = 0
    
    ## Invalid input
    else:
        print("Input suitable option\n")

    ## Print list of available methods
    print("Debug features: " + str(s.system.listMethods()))
    print()