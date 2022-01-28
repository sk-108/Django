print("statement-1")
try : 
    print(10/0)
except ZeroDivisionError as msg :
    print('Exception raised is ',msg)
    print(10/2)
print("statement-2")
# The code that may rise an exception is called risky code
# except(ZeroDivisionError,ValueError) as msg :     for multiple error   
# except : for any type of error 
# finally : compulsory excute either exception raised or not raised (Resource deallocation Code (clean up code ))
''' 
try : 
    risky code 
except : 
    handling code 
finally : 
    clean up code 
'''
