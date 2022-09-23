import sys
sys.path.append("E:/Automation/Practice/Module_Package/Package1")
sys.path.append("E:/Automation/Practice/Module_Package/Package1/Package2")

from Package1 import Module1
from Package1.Package2 import Module2

Module1.display()

Module2.show()
