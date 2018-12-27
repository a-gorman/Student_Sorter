class Course:
    def __init__(self,name,maxsize):#,position):
        self._name = name
        self._max_size = maxsize
        self._students = []
        #self.position = position #Position within the table

    def is_full(self):
        return len(self._students) >= self._max_size

    def max_size(self):
        return self._max_size

    def add_student(self,student):
        if not self.is_full:
            self._students.append(student)
            return True
        else:
            return False