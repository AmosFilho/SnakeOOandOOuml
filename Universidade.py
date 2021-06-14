from Departamento import Department


class University:
    def __init__(self, uni_name, address, rector):
        self.uni_name = uni_name
        self.address = address
        self.rector = rector
        self.departments = []

    def insert_department(self, departmentx: Department):
        self.departments.append(departmentx)

    def list_departments(self):
        print(self.uni_name, "\nEndereço:", self.address, "\nReitor:", self.rector)
        for department in self.departments:
            print("Departamento:", department.dname, "\nBloco:", department.sectors)
            for professor in department.professors_list:
                print("Professor:", professor.pname)
