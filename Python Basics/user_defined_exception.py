class TooYoungException(Exception) : 
    def __init__(self,x) : 
        self.msg = x 

class TooOldException(Exception) : 
    def __init__(self,x) : 
        self.msg = x
    
age = int(input('Enter age'))
if age > 60 : 
    raise TooYoungException('plz wait some more time ... you will get best match ')
elif age < 18 : 
    raise TooOldException('Your age already crossed marriage age... No chance of getting marraiage ')
else : 
    print('You will get match details soon by email ')

# checked exception , throws these concepts are not applicable here as 
# it is interpreted language not compiled language
