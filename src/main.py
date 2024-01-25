from sll import SLL, SLLNODE
from dll import DLL, DLLNODE


node = SLLNODE()
print(node.get_data())
node.set_data(7)
print(node.get_data())
node2 = SLLNODE('carrot')
print(node.get_next())