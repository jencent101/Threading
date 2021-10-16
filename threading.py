from threading import Thread
from random import choice
import time
 
data = [90,81,78,95,79,72,85]

class MyThread(Thread):
 
    def __init__(self, val):
        # Costructor
        Thread.__init__(self)
        self.val = val
 
 
    def run(self):
        for i in range(1):
            time.sleep(2)
            print('Average Value:',choice(data),'in %s' % (self.getName()))
            print('Maximum Value:',choice(data),'in %s' % (self.getName()))
            print('Minimum Value:',choice(data),'in %s' % (self.getName()))

 
 
# Run following code when the program starts
if __name__ == '__main__':
    print('Thread Starting...')
   # Declare objects of MyThread class
    myThreadOb1 = MyThread(3)
    myThreadOb1.setName('Thread 1')
    
    myThreadOb2 = MyThread(3)
    myThreadOb2.setName('Thread 2')

    myThreadOb3 = MyThread(3)
    myThreadOb3.setName('Thread 3')
    
    # Start running the threads!
    myThreadOb1.start()
    myThreadOb2.start()
    myThreadOb3.start()

    # Wait for the threads to finish...
    myThreadOb1.join()
    myThreadOb2.join()
    myThreadOb3.join()

    print('Thread Terminating...')