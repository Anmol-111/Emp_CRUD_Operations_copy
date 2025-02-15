import sys
sys.path.append(
    "C:\\Users\\Anmol\\Desktop\\EmpCRUDapplication\\Bussiness_Entities")
sys.path.append(
    "C:\\Users\\Anmol\\Desktop\\EmpCRUDapplication\\Data_Access_Layer")
import Emp_Entities as Bent 
import EmpDB as Edb 

class CEmpBal:
    """Bussiness Access Layer"""

    def mInsert_Data(self, obj_ent=Bent.CEmpEntities()):
        obj_db = Edb.CEmpDB()
        dictionary={"Emp Id":obj_ent.get_emp_id(),
                    "First Name":obj_ent.get_f_name(),
                    "Last Name":obj_ent.get_l_name(),
                    "Age":obj_ent.get_age(),
                    "Sex":obj_ent.get_sex(),
                    "Salary":obj_ent.get_salary()}
        print("Data for Insertion:",dictionary)
        option=input("Do you want to insert this data?(Yes/No):").upper()
        if option=="YES":
            obj_db.m_Connect_Sql()
            obj_db.m_Insert_Data(obj_ent)
        elif option=="NO":
            print("Insertion of data is not permitted.")
        else:
            print("Please enter the valid option(Yes/No)")
    
    def mUpdate_Data(self, obj_ent=Bent.CEmpEntities()):
        obj_db = Edb.CEmpDB()
        dictionary={"Emp Id":obj_ent.get_emp_id(),
                    "First Name":obj_ent.get_f_name(),
                    "Last Name":obj_ent.get_l_name(),
                    "Age":obj_ent.get_age(),
                    "Sex":obj_ent.get_sex(),
                    "Salary":obj_ent.get_salary()}
        print("Data for updation:",dictionary)
        option=input("Do you want to update this data?(Yes/No):").lower()
        if option=="yes":
            obj_db.m_Connect_Sql()
            obj_db.m_update_table(obj_ent)
        elif option =="no":
            print("Updation of data is not permitted.")
        else:
            print("Enter the valid option(Yes/No).")
    
    def mDelete_Data(self, obj_ent=Bent.CEmpEntities()):
        obj_db = Edb.CEmpDB()
        obj_db.m_Connect_Sql()
        obj_db.m_delete_table(obj_ent)
        
    def mRetrieval_Data(self):
        obj_db=Edb.CEmpDB()
        obj_db.m_Connect_Sql()
        obj_db.m_retrieval_table()
        
    def mFilter_Data(self,obj_ent=Bent.CEmpEntities()):
        obj_db=Edb.CEmpDB()
        obj_db.m_Connect_Sql()
        obj_db.m_filter_table(obj_ent)