#ชื่อ,เงินเดือน
class Employee: #การสร้างcalss
   #  สร้าง methosd
   1 def detail (self,name ,salary ,department) :
        #สร้าง Attribte
        self.name = name
        self.salary = salary
        self.departmet = department

    def showData(self):
        print( 'ชื่พนักงาน = {}' .format(self.name))
        print('งินเดือน = {}'.format(self.salary))
        print('แผนก = {}' .format(self.salary))

#Attribute เป็นกลไกลที่กำหนดคูณสมบัติให้กับ class
#การสร้างAttribute
 # self.name = ชื่อพนักงาน
 # self.salary = เงินเดือน
 # self.age = อายุของพนักงาน
# Method เป็นกลไกที่กำหนดพฤติกรรมให้กับ class
# การสร้าง Method
#   def getName(self)
#       return self.name
# การเรียกใช้งาน
#   ชื่อวัตถ.getName()
#conatructior
#เป็น methd
# คีย์เวิร์ด self
#   การใช้คีย์เวิร์ด self จะเป็นตัวชี้หรือบ่งบอกว่าตอนนี้เราทำงานกับวัตถุใด
#ให้อกตัาตนของวัตถุนั้น ๆ เช่ย การกำหนดดุณสมบัติต่าง ๆ ในวัตถุ เป็นต้บ
#การสร้างวัตถุ

emp1=Employee()
emp1.detail('สกุณภัทรา',5000,'กรรทก่ารผัูจัดการ')
emp1 .showData()

emp2=Employee()
emp2.detail('ชนภุสลุง',25000,'ฝ่่ผลิต')
emp2 .showData()

emp3=Employee()
emp3.detail('แอล',20000,'ฝ้ายบรหาร')
emp3 .showData()