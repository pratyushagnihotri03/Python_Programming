import threading


class ChatMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = ChatMessenger(name='Thread 1: Send out message')
y = ChatMessenger(name='Thread 2: Receive message')
x.start()
y.start()