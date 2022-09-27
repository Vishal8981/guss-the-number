# guss the number is correct or not in less than 9 attempt

n=15
n_of_gusses=1
while(n_of_gusses<=9):
    n_guss=int(input("Enter the number to be gusses: "))
    if(n_guss>n):
        print("You enter the larger number please enter the smaller number")
    elif(n_guss<n):
        print("You enter the smaller number please enter the larger number")
    else:
        print("you enter the correct number")
        print(n_of_gusses,"the number of gusses done to get the correct output")
        break
    print(9-n_of_gusses,"number of gusses left")
    n_of_gusses=n_of_gusses+1
if(n_of_gusses>9):
    print("your gussing chance is over ")
