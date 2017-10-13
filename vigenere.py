import sys

def cipher(key,filein, fileout):
    key.split()
    master = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',' ','.',',','!','?','$','&',';',':','"']
    master_key = [] #Master list that the sub lists will be saved to
    for i in key:
        sub_key = [] #sub list for each letters from the key
        p = master.index(i) # Finds position from master letter list
        for r in master[p:-1]: #This starts from the index position from the last command and adds it to the sub list
            sub_key += r
        for t in master[0:p]: # This for loop starts at the beginning of the master list and goes till it reaches the start point
            sub_key.append(t) # This adds to the rear of the new sub list
        master_key += [sub_key] #This adds the sud_list based off the key word into the master_key list
    return(master, master_key, key, filein, fileout) # Outputs the results, so it can be piped into other functions

def encode(master, master_key, key, filein, fileout): # Encodes file into cryptographic form, receives agruments from cipher func and start func
    try: # This tries to open and use the input file provided from start func
        fin = open(filein, 'r') # Reads the input file
        out = open(fileout, 'w') # Creates output file
        o = fin.read() # Reads the entire text from the file
        o = o.strip() #removes \n character from text file while scanning for index positions
        o.split() # breaks apart strings for for loop scanning
        if o.startswith('Decoded: ') == True: # If youre using a already decoded or encoded file, this will strip the header data 
            o = o.strip('Decoded: ')
        elif o.startswith('Encoded: ') == True:
            o = o.strip('Encoded: ')
        enc = '' # Empty string for dumping crypto strings
        enw = 'Encoded: ' # Header info when the file is done
        i = 0 # Iterator for string count for cycling through master key lists
        for u in o: # Scans through file strings
            p = master.index(u) # position of the character
            enc += master_key[i][p] # i variable controls which sub list in master_key to cycle through and P controls that character at the position and adds it to the empty str
            i += 1 # Adds to the Iterator
            if i >= len(key) or i >= len(o): # If i equals the legnth of key or o, the counter restarts allowing for cycling through master_key sublist
                i = 0
            if len(enc) == len(o): # Once the empty string equals the length of the orignal file, the if conditional will activate
                encfinal = enw + enc # This concatenates the Encoded message with the completed string
                out.write(encfinal) # Writes to output file
                out.close() # Closes output
                fin.close() # Closes original input
                print("\n" + encfinal)# Prints final encoded message with newline characters 
                final = '\n' # Creates a empty string for displying master_key sub list
                for e in range(len(master_key)): # This prints the cryptographic master_key sub lists
                    for z in master_key[e]:
                        final += z # Copies from master_key lists and adds them to final as strings and gives each line its own row
                    final += '\n' # Adds a newline so the words dont blend with the command line
                print(final)    
    except: # If the try func fails to open the input file due to it being not found or error it will display this message
        print("\n" + "Input file is invalid or not found. Please try again." + "\n")    

def decode(master, master_key, key, filein, fileout): # Decodes file into plain text form
    try: # This tries to open and use the input file provided from start func
        fin = open(filein, 'r')
        out = open(fileout, 'w')
        o = fin.read()
        o = o.strip() #removes \n character from text file while scanning
        o.split()
        if o.startswith('Decoded: ') == True:
            o = o.strip('Decoded: ')
        elif o.startswith('Encoded: ') == True:
            o = o.strip('Encoded: ')
        dec = ''
        dew = 'Decoded: '
        i = 0
        for u in o:
            p = master_key[i].index(u) # Since were decoding we pull index positions from the master_key list instead of the orignal master list
            dec += master[p] # Takes the index position from variable p and grabs the character from the index position from the master list 
            i += 1
            if i >= len(key) or i >= len(o):
                i = 0
            if len(dec) == len(o):
                decfinal = dew + dec
                out.write(decfinal)
                out.close() 
                fin.close()
                print('\n' + decfinal)
                final = '\n'
                for e in range(len(master_key)):
                    for z in master_key[e]:
                        final += z
                    final += '\n'
                print(final)
    except: # If the try func fails to open the input file due to it being not found or error it will display this message
        print("\n" + "Input file is invalid or not found. Please try again." + "\n")


def start(): # Command line start
    en_de = sys.argv[1] # Assigns agrument 1 to encode -e or decode -d to variable 
    if len(en_de) == 2: # Tests whether the agrument is valid based off of length, main func checks if its e or d strings
        filein = sys.argv[2] # Assigns file input from agrument
        if '.encode' in filein or '.decode' in filein: # Tests whether the agrument is valid and if the user is using the file format i want
            fileout = sys.argv[3] # Assigns file output from agrument 
            if '.encode' in fileout or '.decode' in fileout: # Tests whether the agrument is valid and if the user is using the file format i want
                if sys.argv[-1] != " ": # Makes sure key isn't empty
                    key = sys.argv[-1] #Assignes key variable
                    if len(key) >= 3: # Test if the key length is great or equal to three
                        if __name__ == '__main__': # Test sys argv func to actiavte main func 
                            main(en_de, filein, fileout, key) # passes this newly assigned variables to the main func for later use
                    else:
                        print("\nYou must have three of more key values.\n") # Key error due to length
                else:
                    print("\nPlease enter a key value for crypo scale.\n") # Key error due to empty string 
            else:
                print("\nPlease enter the correct file format for this OUTPUT file. I.E. <Filename>.encode or <Filename>.decode\n") # Output error
        else:
            print("\nPlease enter the correct file format for this INPUT file. I.E. <Filename>.encode or <Filename>.decode\n") # Input error
    else:
        print("\nPlease specify whether you would like to encode(-e or -E) or decode(-d or -D).\n") # Encoding and decoding error if not specified

def main(en_de, filein, fileout, key): # Receives inputs from start() cmd line agruments
    if en_de == "-e" or en_de == "-E": # Test if you want to encode and if you inputted a valid encoding argument
        (master, master_key, key, filein, fileout) = cipher(key, filein, fileout) 
        encode(master, master_key, key, filein, fileout)
    elif en_de == "-d" or en_de == "-D": # Test if you want to decode and if you inputted a valid decoing agrument
        (master, master_key, key, filein, fileout) = cipher(key, filein, fileout) # Pipes variables from start func into cipher func and assigns them to variables
        decode(master, master_key, key, filein, fileout) # Inputs assigned varibales into decode oe encode func
    else:
        print('\n' + en_de + " in not a valid agrument. Please enter either (-e or -E) for encoding or (-d or -D) for decoding.\n") # Error if user input is not valid

start() # initial startup of the program
