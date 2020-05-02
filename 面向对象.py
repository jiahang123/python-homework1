class Person():
    name = "noname"

    def get_name(self):
        return self.name


print(Person.name)
p = Person()
print(p.name)
print(p.get_name())
# p.name="lili"
p.name = "xiaoming"
Person.name = "lili"
print(p.name)
p1 = Person()
print(p1.name)
