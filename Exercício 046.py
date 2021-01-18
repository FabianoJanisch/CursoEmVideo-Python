import time
print ('Fogos em...')
for fogos in range(10, -1, -1):
    print (f'{fogos} segundos')
    time.sleep(1)
print ("BOOOOM")