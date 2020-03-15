from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key
import threading
from time import sleep
import sys

delay = float(input("Delay: "))
print("INSTRUCTION: Press \"Control Right\" to toggle the auto clicker, Press \"Delete\" to exit\n")

toggle_key = Key.ctrl_r
exit_key = Key.delete

mouse = Controller()

class Click(threading.Thread):
    def __init__(self):
        super().__init__()
        self.toggled = False
        self.running = True

    def on(self):
        print("Auto Clicker ON")
        self.toggled = True

    def off(self):
        print("Auto Clicker OFF")
        self.toggled = False

    def quit(self):
        print("\nSuccessfully exited")
        self.running = False
        self.toggled = False
    
    def run(self):
        while self.running:
            while self.toggled:
                mouse.click(Button.left)
                sleep(delay)

thread = Click()
thread.start()

def on_press(key):
    if key == toggle_key:
        if thread.toggled:
            thread.off()
        else:
            thread.on()
    elif key == exit_key:
        thread.quit()
        listener.stop()
        sys.exit()

with Listener(on_press=on_press) as listener:
    listener.join()


                
