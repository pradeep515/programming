import threading
import time

class testthread(threading.Thread):
    def __init__(self, threadID, threadname):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadname = threadname

    def run(self):
        print("starting" + self.name)
        for i in range(5):
            print(self.threadname)
        print("Exciting" + self.name)

thread1 = testthread(1, "thread1")
thread2 = testthread(1, "thread2")
thread1.start()
thread2.start()
print("Exciting main thread")
