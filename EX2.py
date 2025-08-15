#เขียนโปรแกรมสร้าง class ชื่อ people โดยมี attribute และ Method ดังนี้
#attribute
#age เป็นอายุของบุคคล
#Introduce() เมื่อเรียกใช้จะพิมพ์ข้อความ My name is <name>. I'm <age> year old
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Introduce(self):
        print(f"My name is {self.name}. I'm {self.age} years old.")


person = People("Skunpatra", 19)
person.Introduce()
