import threading

class testThread:

    def __init__(self, num):
        self.num = num

    def task1(self):
        print(self.num * self.num * self.num)
        print("task is assigned to thread {}".format(threading.currentThread().name))

    def task2(self):
        print(self.num * self.num )
        print("task is assigned to thread {}".format(threading.currentThread().name))

    def start_thread(self):

        t1 = threading.Thread(target=self.task1, name='first')
        t2 = threading.Thread(target=self.task2, name='second')
        t1.start()
        t2.start()

if __name__=="__main__":
    t = testThread(5)
    t.start_thread()

        