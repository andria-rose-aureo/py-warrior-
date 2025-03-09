# Student Management System
print("🔹 Welcome to Student Management System 🔹\n 1. Add Student \n 2. View Students \n 3. Update Student Marks \n 4. Delete Student \n 5. Exit")
my_dict = {}
while  True :
    n = int(input("Enter your choice (bw 1 & 5) : "))
    if (n == 1):

        entries = int(input("enter number of students to add: "))
        for i in range(entries):
          key = input("enter name: ")
          value = input("enter age and marks seperated by space: ").split()
          my_dict[key]= value
        print(" records added successfully!")
    elif (n == 2):
        if my_dict:
            print("\n students records : ")
            for key, value in my_dict.items():
                print(f"* name : {key}, age :{value[0]}, marks :{value[1]}")
        else:
            print("no records")
    elif (n == 3) :
        name = input("enter the name of the student mark to be updated : ")
        if name in my_dict:
             updated_marks = input("enter the marks to be updated : ")
             my_dict[name][1]= updated_marks
             print("✅ Marks Updated Successfully!")
        else:
            print("no student records!!")
    elif(n==4):
        name = input("enter the name of the student mark to be deleted : ")
        if name in my_dict:
           del my_dict[name]
           print("✅ student deleted Successfully!")
        else:
           print("no student records")
           
        print(" Exiting... Thank you for using Student Management System! ")
        break

    else :
        print("Enter a num bw 1 to 5")