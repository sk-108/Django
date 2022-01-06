'''import modules

modules.connect()
modules.message("sourav")
modules.disconnect()'''
# to optimize writing we can use
'''from modules import * 
connect()
message("sourav")
disconnect()
'''
from modules import connect as c,message as m,disconnect as dc
c()
m("hare krishna sourav reading mat bulna ")
dc()