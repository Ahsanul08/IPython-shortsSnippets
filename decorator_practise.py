import time

def timecalc(func):
    
    def wrapper():
        t = time.clock()
        res = func()
        print func.func_name, time.clock() - t 
        return res   
    return wrapper  
    

@timecalc
def my_func():
    time.sleep(1)
    print "Idle Function"


my_func() 
