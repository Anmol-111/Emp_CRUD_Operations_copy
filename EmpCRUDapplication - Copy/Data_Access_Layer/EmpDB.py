import pymysql
import sys
sys.path.append(
    "C:\\Users\\Anmol\\Desktop\\EmpCRUDapplication\\Bussiness_Access_Layer")
sys.path.append(
    "C:\\Users\\Anmol\\Desktop\\EmpCRUDapplication\\Bussiness_Entities")

import EmpBAL as bal
import Emp_Entities as Bent

class CEmpDB:
    
    """Employee Database connectivity Class."""

    def m_Connect_Sql(self):
        global constr, cursor
        constr = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='testdb'
        )
        cursor = constr.cursor()

    def m_Insert_Data(self, obj_ent=Bent.CEmpEntities()):
        cursor.execute('''
                CALL sp_insert_data(%s,%s,%s,%s,%s,%s);
                ''', (obj_ent.get_emp_id(), obj_ent.get_f_name(), obj_ent.get_l_name(), obj_ent.get_age(), obj_ent.get_sex(), obj_ent.get_salary()))
        constr.commit()
        constr.close()
        
        
    def m_update_table(self, obj_ent=Bent.CEmpEntities()):
        data = cursor.execute('''
                CALL sp_update_data(%s,%s,%s,%s,%s,%s);    
                ''', (obj_ent.get_f_name(), obj_ent.get_l_name(), obj_ent.get_age(), obj_ent.get_sex(), obj_ent.get_salary(), obj_ent.get_emp_id()))
        print("Data updation is successfull.")
        constr.commit()
        constr.close()
        
    def m_delete_table(self, obj_ent=Bent.CEmpEntities()):
        data = cursor.execute('''
                CALL sp_delete_data(%s);
                ''', (obj_ent.get_emp_id()))
        print("Deleted Data:",data)
        constr.commit()
        constr.close()
    
    def m_retrieval_table(self):
        cursor.execute('''
                CALL sp_retrieve_alldata;
                ''')
        for data in cursor.fetchall():
            print(data)
        constr.close()
    
    def m_filter_table(self, obj_ent=Bent.CEmpEntities()):
        cursor.execute('''
                CALL sp_retrievefilterdata(%s);
                ''',(obj_ent.get_emp_id()))
        constr.close()
        