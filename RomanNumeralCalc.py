# This code was peer-reviewed by Egan Schmidt Weiss at 6:13 pm on Wednesday, November 3rd, 2021, in the SDC.

key = "y"
while key == "y":

# Input Statements
    var1 = input("\nEnter a Roman Numeral: ") ; var1 = var1.lower()
    var2 = input("Enter a second Roman Numeral: ") ; var2 = var2.lower()
    var1_set = set(list(var1)) ; var2_set = set(list(var2))

# Dictionary for Numerals
    numerals = {
        "i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5, "vi": 6, "vii": 7, "viii": 8, "ix": 9, "x": 10,
        "xx": 20, "xxx": 30, "xl": 40, "l": 50, "lx": 60, "lxx": 70, "lxxx": 80, "xc": 90,
        "c": 100, "cc": 200, "ccc": 300
    }
# Dictionary for Converting back to Numerals
    convert = {
        3 : 100, 2 : 10, 1 : 1,
    }

# Required Lists for Appending
    flag = [] ; vara = [] ; varb = [] ; some_list = [] ; answer =[]

# Checking for Valid Roman Numerals
    list_of_var1 = list(var1)
    list_of_var2 = list(var2)
    all_list = list_of_var2 + list_of_var1
    for i in all_list:
        if i not in numerals:
            flag.append(0)
        else:
            flag.append(1)

    if all(flag) == 1:

# If valid Numerals Run Code
# Convert Input to Integers
        i=len(var1)
        while i>0:
            vara.append(numerals.get(var1[i-1:i]))
            i -= 1

        vara.reverse()

        output1 = 0
        output2 = 0
        i = 0
        while i < len(vara):
            if vara[i:i+1] >= vara[i+1:i+2]:
                output1 += sum(vara[i:i+1])
                i += 1
            elif vara[i:i+1] < vara[i+1:i+2]:
                output2 += abs(min(vara[i:i+1]) - min(vara[i+1:i+2]))
                i += 2       

        i=len(var2)
        while i>0:
            varb.append(numerals.get(var2[i-1:i]))
            i -= 1

        varb.reverse()

        output3 = 0
        output4 = 0
        i = 0
        while i < len(varb):
            if varb[i:i+1] >= varb[i+1:i+2]:
                output3 += sum(varb[i:i+1])
                i += 1
            elif varb[i:i+1] < varb[i+1:i+2]:
                output4 += abs(min(varb[i:i+1]) - min(varb[i+1:i+2]))
                i += 2       

        input1 = str(output1 + output2 + output3 + output4)

# Convert Integers back to Numerals
        full = len(input1)
        while full > 0:
            for i in input1:
                some = int(i) * convert.get(full)
                some_list.append(some)
                full -= 1

        for i in some_list:
            for key, value in numerals.items():
                if i == value:
                    answer.append(key)
# Print Answer
        answer = "".join(answer)
        print("------------------")
        print(answer.upper())
        print("------------------")
# If not Valid Numerals
    else:
        print()
        key = input("Sorry, a roman numeral you entered isn't a roman numeral\n\nWould you like to try again? (y/n) ")

    key = input("Would you like to go again? (y/n) ")
