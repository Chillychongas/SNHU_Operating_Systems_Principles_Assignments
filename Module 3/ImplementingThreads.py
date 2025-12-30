"""
Author: Andrew Ferasol
Due Date: 11/30/2025
Description: Create functions to utilize threads and see how they act
"""
import threading
import time


#2 functions with 2 different delays to show how threads deal with concurrency 
def threadTest_2seconds(name):
	print(f"{name}: Function Call Opening")
	time.sleep(2)
	print(f"{name}: Function Call Closing")
	
def threadTest_3seconds(name):
	print(f"{name}: Function Call Opening")
	time.sleep(3)
	print(f"{name}: Function Call Closing")


t1 = threading.Thread(target = threadTest_2seconds, args = ("Thread 1",))
t2 = threading.Thread(target = threadTest_3seconds, args = ("Thread 2",))
t3 = threading.Thread(target = threadTest_2seconds, args = ("Thread 3",))

t1.start()
t2.start()

t1.join()

t3.start() 

t2.join()
t3.join()