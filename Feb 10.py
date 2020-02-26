class Employee:
    def __init__(self,emp_id,emp_name,emp_rol,emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_rol = emp_rol
        self.emp_salary = emp_salary
    
    def increment(self,emp_inc):
        self.emp_salary+=(self.emp_salary*emp_inc)//100

class Organisation:
    def __init__(self,org_name,emp_list):
        self.org_name = org_name

    def rol_inc(self,emp_rol,emp_inc):
        b = []
        for i in emp_list:
            if i.emp_rol == emp_rol:
                i.increment(emp_inc)
                b.append(i)
        return b
    
if __name__=='__main__':
    emp_list = []
    count = int(input())
    for i in range(count):
        emp_id = int(input())
        emp_name = input()
        emp_rol = input()
        emp_salary = int(input())
        emp_list.append(Employee(emp_id,emp_name,emp_rol,emp_salary))
    o = Organisation('ABC',emp_list)
    emp_rol = input()
    emp_inc = int(input())
    res = o.rol_inc(emp_rol,emp_inc)
    for j in res:
        print(j.emp_name)
        print(j.emp_salary)
    
