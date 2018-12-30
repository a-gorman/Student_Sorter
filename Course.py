class Course:
    def __init__(self,name,maxsize):
        self._name = name
        self._max_size = maxsize
        self._students = []

    def is_full(self):
        return len(self._students) >= self._max_size

    def max_size(self):
        return self._max_size

    def add_student(self,student):
        if not self.is_full():
            self._students.append(student)
            return True
        else:
            return False

    def to_csv(self):
        string = self._name
        if(self._students == 0):
            return string
        
        for student in self._students:
            string = string + r',' + student

        return string
