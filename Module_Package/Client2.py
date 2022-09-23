import sys
sys.path.append("E:/Automation/Practice/Module_Package/Pck1")
sys.path.append("E:/Automation/Practice/Module_Package/Pck2")

from Pck1 import Emp
from Pck2 import Stu

obj1 = Emp.Employee(1,"Reshma",3500000)
obj1.displayEmp()

obj2 = Stu.Student(1,"ReshuMoorthy","A")
obj2.displaystu()
