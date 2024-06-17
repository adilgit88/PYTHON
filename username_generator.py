

ch = int(
    input(
        "do you want to generate a username with your name ?(1), OR username without your name : "
        ))
vowels = ['a','e','i','o','u']
if ch == 1:
    name = input("Enter your First Name : ").lower()
    lastn= input("Enter your Last Name: ").lower()
    bday = input("Enter your birth-date (only day)")
    pwd = ""
    for l in name :
     # if l in vowels :
    # l = l.capitalize()
        pwd += l
    pwd=pwd + "_"
    for l in lastn:
    #if l in vowels:
    # l=l.capitalize()
     pwd += l
    pwd = pwd + "_" + bday
    print(pwd)
elif ch == 2:
    fav_adj = input("Enter adjective: ").lower()
    fav_animal = input(
        "enter your favourite animal/cartoon/character: ").lower()
    fav_num = input("enter your favourite number: ")
    pwd = fav_adj + "_" + fav_animal + "_" + fav_num
    print(pwd)
else:
    print("invalid input")