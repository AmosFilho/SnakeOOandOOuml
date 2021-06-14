class Department:
    professors = []

    def __init__(self, dname, sectors):
        self.professors_list = []
        self.dname = dname
        self.sectors = sectors

    def add_professor(self, professor):
        self.professors_list.append(professor)
