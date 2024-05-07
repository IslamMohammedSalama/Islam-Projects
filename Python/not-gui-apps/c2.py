# print("resalt is : ", float(eval(input("enter your opration type : "))) , ".ckgjh")
import threading

def func1():
    print("Function 1 is running")

def func2():
    print("Function 2 is running")

# Create threads for each function
thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=func2)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()


