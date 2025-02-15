import sys
sys.path.append(
    "C:\\Users\\Anmol\\Desktop\\EmpCRUDapplication\\Bussiness_Access_Layer")
sys.path.append(
    "C:\\Users\\Anmol\\Desktop\\EmpCRUDapplication\\Bussiness_Entities")
import EmpBAL as EBal
import Emp_Entities as Bent

obj_bal = EBal.CEmpBal()

choice="yes"
while choice=="yes":
    print("Operations :\n 1. Insert \n 2. Update \n 3. Delete \n 4. Retrieval \n\t4.1. Whole table \n\t4.2. specific row")
    option = float(input("Enter the choice (1-4):"))
    if option == 1:
        obj_ent = Bent.CEmpEntities()
        emp_id = int(input("Enter the Emp_id:"))
        obj_ent.set_emp_id(emp_id)
        fname = input("Enter the first name:")
        obj_ent.set_f_name(fname)
        lname = input("Enter the last name:")
        obj_ent.set_l_name(lname)
        age = int(input("Enter the age:"))
        obj_ent.set_age(age)
        sex = input("Enter the sex (M/F/T):")
        obj_ent.set_sex(sex)
        salary = float(input("Enter the salary:"))
        obj_ent.set_salary(salary)
        obj_bal.mInsert_Data(obj_ent)
    elif option == 2:
        obj_ent = Bent.CEmpEntities()
        emp_id = int(input("Enter the Emp_id for updation:"))
        obj_ent.set_emp_id(emp_id)
        fname = input("Enter the first name for updation:")
        obj_ent.set_f_name(fname)
        lname = input("Enter the last name for updation:")
        obj_ent.set_l_name(lname)
        age = int(input("Enter the age for updation:"))
        obj_ent.set_age(age)
        sex = input("Enter the sex (M/F/T) for updation:")
        obj_ent.set_sex(sex)
        salary = float(input("Enter the salary for updation:"))
        obj_ent.set_salary(salary)
        obj_bal.mUpdate_Data(obj_ent)
    elif option == 3:
        obj_ent = Bent.CEmpEntities()
        emp_id = int(input("Enter the Emp_id for Deletion:"))
        obj_ent.set_emp_id(emp_id)
        obj_bal.mDelete_Data(obj_ent)
    elif option == 4:
        option=float(input("Enter the option for Retrieval:"))    
        if option == 4.1:
            obj_bal.mRetrieval_Data()
        elif option == 4.2:
            obj_ent=Bent.CEmpEntities()
            emp_id = input("Enter the Emp_id for Retrieval:")
            obj_ent.set_emp_id(emp_id)
            obj_bal.mFilter_Data(obj_ent)
    else:
        print("Please enter the valid option.")
    choice=input("Do you want to perform more operations(Yes/No) :").lower()