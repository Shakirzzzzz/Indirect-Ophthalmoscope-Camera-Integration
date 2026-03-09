from picamera2 import Picamera2,Preview
from libcamera import controls


class CameraController:
    def __init__(self,main_size=(1920,1080),lores_size=(640,480),framerate=30):
        self.main_size = main_size
        self.lores_size = lores_size
        self.framerate = framerate
        self.camera = Picamera2()
        self._configure_camera()
    
    def _configure_camera(self):
        video_config = self.camera.create_video_configuration(
            main={"size":self.main_size},
            lores={"size":self.lores_size},
            controls={"FrameRate": self.framerate}
        )
        self.camera.configure(video_config)
    
    def start(self):
        self.camera.start_preview(Preview.DRM)
        self.camera.start()
    
    def stop(self):
        self.camera.stop_preview()
        self.camera.stop()
    
    def get_camera(self):
        return self.camera
    
    def enable_continuous_autofocus(self):
        self.camera.set_controls({"AfMode": controls.AfMode.Continuous})
