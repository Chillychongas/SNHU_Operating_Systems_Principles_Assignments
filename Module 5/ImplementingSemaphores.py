'''
Author: Andrew Ferasol
Due Date: 12/14/2025
Desc.:
a simple python program to demonstrate the use of a semaphore
'''
import threading
import random
import time


#init the semaphore with the max number of processes being arbitrarily 3
MAX_PROCESSES = 3
semaphore = threading.Semaphore(MAX_PROCESSES)
'''
NOTE: threading library has another semaphore class called ".BoundedSemaphore"
which handles .acquire() and .release() making things easier on the programmer
'''

#function to mimic work being done
def artificial_delay(pid):
	print(f"Process {pid}: waiting to acquire semaphore")
	
	semaphore.acquire()
	try:
		print(f"Process {pid}: ENTERING critical section")
		#output statement to see the max number of "processes" happening
		print(f"Active processes: {MAX_PROCESSES - semaphore._value}" )
		
		time.sleep(random.randint(1,6))
		
		print(f"Process {pid}: EXITING critical section")
	finally:
		semaphore.release()
	
	
threads = []

for i in range(1,6): #double the amount of allowed processes at one time
	thread = threading.Thread(target = artificial_delay, args = (i,))
	threads.append(thread)
	thread.start()
	
	
for thread in threads:
	thread.join()
	
print("Finished")

