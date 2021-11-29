password = "baseball"
pwd_not_found = ""

file1 = open('10k most common.txt', 'r')
Lines = file1.readlines()

for line in Lines:
    txt = line.strip()

    if txt == password:
        print("The Password is : "+txt)
        pwd_not_found = "No"
        break 
    else:
        pwd_not_found = "Yes"   

file1.close()

if pwd_not_found == "Yes":
    print("Password Not Found!")