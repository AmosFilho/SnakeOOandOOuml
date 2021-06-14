from Disciplina import Subject
from Professor import Professor
from Departamento import Department
from Universidade import University

materia = Subject("Lab", "18:00")
prof1 = Professor("Jucimar")
prof1.subject = materia
department1 = Department("Ciências Exatas", "A")
department1.add_professor(prof1)
university_am = University("UEA", "Darcy Vargas", "Cleinaldo Costa")
university_am.insert_department(department1)
university_am.list_departments()
