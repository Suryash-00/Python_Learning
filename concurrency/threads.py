import time
#from threading import Thread
from concurrent.futures import ThreadPoolExecutor   #creates collection of threads

def ask_user():
    start= time.time()
    user_input= input("Enter your name:")
    greet= f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time()-start}')

def complex_calculation():
    start= time.time()
    print("Started calculating....")
    [x**2 for x in range(20000000)]
    print(f'complex_calculation, {time.time()-start}')

start= time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time()-start}')

'''
thread1= Thread(target=ask_user())
thread2= Thread(target=complex_calculation())
'''
start= time.time()

with ThreadPoolExecutor(max_workers=2) as pool:     #create two threads in this collection of threads
    pool.submit(complex_calculation)
    pool.submit(ask_user)
'''
thread1.start()
thread2.start()

thread1.join()      #to let the thread1 start before the main thread
thread2.join()      #to let the thread2 start before the main thread
'''
print(f'Two threads total time: {time.time()-start}')