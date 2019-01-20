import re #import regular expression module

def patterns(infile): #define function - take one argument, must be a file
    fa = open(infile, "r") #opens input file, names it fa
    for line in fa.readlines(): #for each line in fa read line for line
        line = line.strip() #removes new line character, names lines line
        if (re.search(r'^(TTG)|(GTT)$',line,re.I)): #regular expression, find all line that begin with "TTG" or end with GTT, search line, ignore case
            print ('Begins with "TTG" or ends with reverse:', line) #prints lines that match
        if (re.search(r'^(TTG)+(GTT)$',line,re.I)): #regular expression, find all line that begin with "TTG" and end with GTT, search line, ignore case
            print('Begins with "TTG" and ends with reverse:', line)
        if (re.search(r'^(TTG)',line,re.I)): #regular expression, find all line that begin with "TTG", search line, ignore case
            print('Begins with "TTG":',line)
        if (re.search(r'[CGA]T{6}[CGA]*|[TGA]C{6}[TGA]*|[TCA]G{6}[TCA]*|[CGT]A{6}[CGT]*',line,re.I)): #regular expression, find lines that have exactly 6 repitions of the same character, * means 0 or more times, finds line that ends with the repition, search line, ignore case
            print('Contains 6 sequential repetitions:',line)
        if (re.search(r'(ATGC)(AT|CG|AG|CT)A',line,re.I)): #regular expression, find all line that contains motif that starts with ATGC followed by AT,CG, AG, or CT and ends with A, search line, ignore case
            print('Motif (ATGC, "AT","CG","AG",or"CT", A):',line)


file = input("Please enter filename: ") #askes user to input file, names it file
if file == "hw6.fa": #if user input equals "hw6.fa, call function on file
    patterns(file)

else: #if user puts in anything besides "hw6.fa"
    defaultfile = "hw6.fa" #sets "hw6.fa file and default file to be processed
    print('Default file "hw6.fa" used: '+'\n')
    patterns(defaultfile) #uses default file 


