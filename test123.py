import time
for x in range (0,4):  
    b = "Running" + "." * x
    print (b, end="\r")
    time.sleep(1)