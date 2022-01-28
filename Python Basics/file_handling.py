f = open('abc.txt','w') # if file not present it will create one
f.write('hare\n')
f.write('krishna\n')
f.write('jai srila prabhupada ji ')
f.close()

f = open('abc.txt','r')
data = f.read()
print(data) 