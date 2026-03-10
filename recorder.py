from datetime import datetime
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
class Recorder:
    def __init__(self,camera,bitrate=20000000):
        self.camera = camera
        self.encoder = H264Encoder(bitrate=bitrate)
        self.output = None
        self.recording = False
    
    def start_recording(self):
        if self.recording:
            print("Already recording")
            return
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"recording_{timestamp}.mp4"
        self.output = FfmpegOutput(filename)
        self.camera.start_encoder(self.encoder,self.output)
        self.recording = True
    
    def stop_recording(self):
        if not self.recording:
            print("Not currently recording")
            return
        self.camera.stop_encoder()
        self.recording = False

        

