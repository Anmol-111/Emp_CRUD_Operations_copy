class CEmpEntities:
    """This is for the Employee Information System."""
    __emp_id=0
    __f_name=''
    __l_name=''
    __age=''
    __sex=''
    __salary=0.00
    __filter_col=''
    __filter_data=''
    def __init__(self):
        pass
    def get_emp_id(self):
        return self.__emp_id
    def set_emp_id(self, __emp_id):
        self.__emp_id=__emp_id
    def get_f_name(self):
        return self.__f_name
    def set_f_name(self, __f_name):
        self.__f_name=__f_name
    def get_l_name(self):
        return self.__l_name
    def set_l_name(self, __l_name):
        self.__l_name=__l_name
    def get_age(self):
        return self.__age
    def set_age(self, __age):
        self.__age=__age
    def get_sex(self):
        return self.__sex
    def set_sex(self, __sex):
        self.__sex=__sex
    def get_salary(self):
        return self.__salary
    def set_salary(self, __salary):
        self.__salary=__salary
    def get_filter_col(self):
        return self.__filter_col
    def set_filter_col(self, __filter_col):
        self.__filter_col=__filter_col
    def get_filter_data(self):
        return self.__filter_data
    def set_filter_data(self, __filter_data):
        self.__filter_data=__filter_data