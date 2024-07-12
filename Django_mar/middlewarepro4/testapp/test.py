import time
class Test:
    def __init__(self):
        print('Constructor Execution.....')
    def __del__(self):
        print('Destructor Execution.....')
l = [Test(),Test(),Test()]
time.sleep(5)
print('End of application')