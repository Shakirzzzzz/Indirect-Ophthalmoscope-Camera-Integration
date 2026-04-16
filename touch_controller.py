from gpiozero import Button
class TouchController:
    def __init__(self, recorder, pin=26):
        self.recorder = recorder
        self.button = Button(pin,bounce_time=0.1)
        self.button.when_pressed = self.handle_touch
    def handle_touch(self):
        if self.recorder.recording:
            print("Stopping recording")
            self.recorder.stop_recording()
        else:
            print("Starting recording")
            self.recorder.start_recording()



