#ClassInstanceVeriable

#Class Verible คือ ตัวแปรที่ทำงานภายใน Class
#ส่วนอื่นสามารถเข้าถึงข้อมูลส่วนนี้ได้เลย (static attribute)
#โดยไม่จำเป็นต้องสร้าง Object ขิ้นมา

#instance Veriable คือ ตัวแปรที่อยู่ภายใน object
#สามารถเข้าถึงข้อมูลส่วนนี้ได้โดยต้องสร้าง Object ขึ้นมา



# class variable
class Employee:
    # class variable
    __minSalary = 12000
    __maxSalary = 50000
    _companyName = 'บริษัท XYZ จำกัด'
    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department


    def _showData(self):
        print('ชื่อพนักงาน = {}'+self.__name)
        print('เงินเดือน = {}'+self.__salary)
        print('แผนก = {}'+self.__department)



emp1 = Employee('สกุภัทรา', 50000, 'วิชาการ')
#print('เงินเดือนพนักงานขั้นต่ำ ='+str(Employee._minSalary))
print(Employee._companyName)