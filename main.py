#!/usr/bin/python3
import signal
from camera_controller import CameraController
from recorder import Recorder
from touch_controller import TouchController

def main():
    camera_controller = CameraController()
    camera_controller.start()
    camera = camera_controller.get_camera()
    recorder = Recorder(camera)
    touch = TouchController(recorder, pin=26)
    print("Everything Ready")
    print("Press the button to start/stop recording")
    try:
        signal.pause()
    except KeyboardInterrupt:
        print("Stopping...")
        camera_controller.stop()
        recorder.stop_recording()

if __name__ == "__main__":
    main()

