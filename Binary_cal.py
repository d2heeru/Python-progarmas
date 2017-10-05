def calculation(binary1,binary):
    operation=input("Select any one operation +, -, *, /, <<, >>")
    if operation=="+":
        print(binary_num1+binary_num2)
    elif operation=="-":
        print(binary_num1-binary_num2)
    elif operation=="*":
        print(binary_num1*binary_num2)
    elif operation=="/":
        print(binary_num1/binary_num2)
    elif operation=="<<":
        print(binary_num1<<binary_num2)
    elif operation==">>":
        print(binary_num1>>binary_num2)
    else:
        print("Please Select correct Operation")



program_continue ="YES"
while program_continue=="YES" or program_continue=="yes":
    try:
        binary_num1, binary_num2 = input("Enter Two binary Numbers").split()
        binary_num1 = int(binary_num1, 2)
        binary_num2 = int(binary_num2, 2)
        calculation(binary_num1, binary_num2)
    except:
        print("Please Enter valid Binary Numbers")
    print("Type YES to continue and NO for Exit")
    program_continue = input()
    if program_continue == "NO" or program_continue == "no":
        print("Finished")

