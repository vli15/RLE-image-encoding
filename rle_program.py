#COP3504C
#Vivian Li
import console_gfx

def count_runs(flatData):
    if len(flatData) == 0:
        return 0
    count = 0 #stores number of repeated instances
    c=0
    fifteen = 0
    fifteenCount = 0
    counts = [] #stores aggregate of count
    temp = flatData[0]
    for element in flatData:
        if fifteen == 15:
            fifteenCount +=1
            fifteen = 0
        if element != temp:
            # count += 1
            c+=1
            temp = element
            fifteen = 0
        else:
            fifteen += 1
    return c + fifteenCount + 1

    #//////
    # encoded = encode_rle(flatData) #bytedata
    # bs = ''
    # for i in range(5, len(encoded), 3):
    #     bs += str(encoded[i])
    # print(bs)
    # s = string_to_rle(bs)

def to_hex_string(data):
    # if len(data) != 2*count_runs(data): #it is raw data
    #     print("if")
    #     #convert the raw data to rle
    hexstring = ''
    for i in data:
        if isinstance(i, int):
            if i >= 10:
                hexadecimal = hex(i)  # 15 --> 0xf
                hexstring += hexadecimal[2] #second element of the hex
            else:
                hexstring += str(i) #typecast int to str
        else:
            hexstring += i
        # print(i)
        # hexstring += hex(i)[2]
        # print("success")
    return hexstring

def encode_rle(flat_data): #returns bytes
    if len(flat_data) == 0:
        return 0
    temp = flat_data[0]  # first element of data
    count = 0
    counts = []
    variables = []
    # making list of repeated instances
    for element in flat_data:
        if element == temp:
            # print("if",temp)
            count += 1
        else:
            # print("else",temp)
            counts.append(count)
            # print("count:",count)
            variables.append(temp)
            temp = element
            count = 1
        if count == 15:
            counts.append(count)
            count = 0
            variables.append(element)
    counts.append(count)
    variables.append(temp)
    rle = []
    for i in range(len(variables)):
        if counts[i] != 0:
            rle.append(counts[i])
            # print("counts:", counts[i])
            rle.append(variables[i])
            # print("variables:", variables[i])
    # print(rle)
    # rle data stored in rle list
    # print("rleString:", rlestring)
    mylist = list()
    for letter in rle:
        if isinstance(letter, int):
            mylist.append(letter)
        else:
            mylist.append(int(letter,16))
    # print(mylist)
    return bytes(mylist)

def get_decoded_length(rle_data):
    sum = 0
    for i in range(0,len(rle_data), 2):
        if isinstance(rle_data[i], int):
            sum += rle_data[i]
        else:
            # print(int(rle_data[i], 16))
            sum+=int(rle_data[i], 16)
    return sum

def decode_rle(rle_data):
    listofelements = []
    for index in range(0,len(rle_data), 2): #for every second element in rle_data
        for i in range(rle_data[index]): #for every round
            listofelements.append(rle_data[index+1])
    return bytes(listofelements)

def string_to_data(data_string: str):
    listofdata = []
    for letter in data_string:
        print(letter)
        intletter = int(letter, 16)
        print(intletter)
        listofdata.append(intletter)
    print(listofdata)
    return bytes(listofdata)

def to_rle_string(rleData):
    s = ''
    j=''
    for i in range(0,len(rleData), 2):
        if rleData[i] != 0:
            s += str(rleData[i])
            s+= str(hex(rleData[i+1])[2])
            s+=':'
    j = s[:len(s)-1]
    return j


def string_to_rle(rleString: str):
    #10f:64
    # print("rlestring:",rleString)
    temp = ''
    my_list = []
    for letter in rleString:
        if letter != ':':
            temp += letter
        else:
            hexadecimal = int(temp[len(temp)-1],16) #last element of the temp string should be a single hexadecimal
            rest = int(temp[:len(temp)-1] )#should be the count of how many instances of an element
            temp = ''
            my_list.append(rest)
            my_list.append(hexadecimal)
    hexadecimal = int(temp[len(temp) - 1], 16)
    rest = int(temp[:len(temp) - 1])
    my_list.append(rest)
    my_list.append(hexadecimal)
    # print(my_list)
    return bytes(my_list)

def main():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.TEST_RAINBOW)
    option = 99
    file = ''
    print()
    while option != 0:
        print("\nRLE Menu\n--------")
        print("""0. Exit
1. Load File
2. Load Test Image
3. Read RLE String
4. Read RLE Hex String
5. Read Data Hex String
6. Display Image
7. Display RLE String
8. Display Hex RLE Data
9. Display Hex Flat Data
            """)
        option = int(input("Select a Menu Option: "))
        if option == 0:
            break
        #Accepts a filename from the user and invokes console_gfx.load_file(filename: str)
        elif option == 1:
            print("Enter name of file to load: ", end='')
            input_file = input()
            file = console_gfx.load_file(input_file)

        #Loads console_gfx.TEST_IMAGE
        elif option == 2:
            file = console_gfx.TEST_IMAGE
            print("Test image data loaded.")

        #Reads RLE data from the user in decimal notation with delimiters (smiley example):
        elif option == 3: #RLE string with delimiters
            print("Enter an RLE string to be decoded: ", end='')
            file_with_delimiters = input()
            bytefile = string_to_rle(file_with_delimiters)
            file = bytefile

        #Reads RLE data from the user in hexadecimal notation without delimiters (smiley example):
        elif option == 4: #RLE string without delimiters
            print("Enter the hex string holding RLE data: ", end='')
            file = input()
            print("RLE decoded length:", get_decoded_length(file)) #this is wrong

        #Reads raw (flat) data from the user in hexadecimal notation (smiley example)
        elif option == 5:
            file = input("Enter the hex string holding flat data: ")
            print("Number of runs:", count_runs(file)) #idk this might be wrong too

        #Displays the current image by invoking the console_gfx.display_image(imageData: bytes) method
        elif option == 6:
            print("Displaying image...")
            if file == '':
                print("(no data)")
            else:
                console_gfx.display_image(file)

        #Converts the current data into a human-readable RLE representation (with delimiters)
        #to_rle_string takes in an iterable of rle data
        elif option == 7:
            print("RLE representation: ", end ='')
            if file == '':
                print("(no data)")
            else:
                print(to_rle_string(encode_rle(file)))

        #Converts the current data into RLE hexadecimal representation (without delimiters)
        elif option == 8:
            print("RLE hex values: ", end='')
            if file == '':
                print("(no data)")
            else:
                print(to_hex_string(encode_rle(file)))

        #Displays the current raw (flat) data in hexadecimal representation (without delimiters)
        elif option == 9:
            print("Flat hex values: ", end='')
            if file == '':
                print("(no data)")
            # elif ':' in file:
            #     bytelist = string_to_rle(file)
            #     decoded = decode_rle(bytelist)
            #     s = to_hex_string(decoded)
            #     print(s)
            else:
                f = list(file) #rn it's in a bytefile
                v = to_hex_string(f)
                for i in range(0, len(v), 2):
                    for j in range(0, int(v[i], 16)):
                        print(v[i + 1], end='')
            print()

        else:
            print("Error! Invalid input.")

if __name__ == '__main__':
    main()