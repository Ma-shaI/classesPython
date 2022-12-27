class Student:
    def __init__(self, name):
        self.name = name
        self.present = self.InfoAboutLaptop()

    def print_info(self):
        print(self.name, '=>', end=' ')
        print(self.present.print_info())

    class InfoAboutLaptop:
        def __init__(self):
            self.model = 'HP'
            self.processor = 'i7'
            self.memory = 16

        def print_info(self):
            return  f'{self.model}, {self.processor}, {self.memory}'


student1 = Student('Roman')
student1.print_info()
student2 = Student('Vladimir')
student2.print_info()