class Person():
    name =  'Person name'
    age = 0

    def setPerson(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name)
        print(self.age)

    def birthday(self):
        self.age += 1