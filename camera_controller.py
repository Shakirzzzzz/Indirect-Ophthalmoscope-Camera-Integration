from picamera2 import Picamera2, Preview
from libcamera import controls
from picamera2.encoders import H264Encoder
from picamera2.outputs import PyavOutput

class CameraController:
    def __init__(self, main_size=(1920,1080), lores_size=(640,480), framerate=30):
        self.main_size = main_size
        self.lores_size = lores_size
        self.framerate = framerate
        self.camera = Picamera2()
        self._configure_camera()
        self._setup_live_stream()
    def _configure_camera(self):
        video_config = self.camera.create_video_configuration(
            main={"size":self.main_size},
            lores={"size":self.lores_size},
            controls={"FrameRate": self.framerate}
        )
        self.camera.configure(video_config)
        print(f"Camera has been configured with settings: {self.main_size} video resolution.")
    
    def _setup_live_stream(self):
        self.lores_encoder = H264Encoder(bitrate=5000000)
        self.output = PyavOutput(
            "rtsp://127.0.0.1:8554/cam",
            format="rtsp"
        )

    def start(self):
        try:
            self.camera.start_preview(Preview.NULL)
        except RuntimeError as e:
            self.camera.start_preview(Preview.NULL)
            print(f"Failed to start preview: {e}")
        self.camera.start()
        self.camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})
        self.camera.start_encoder(self.lores_encoder, self.output, name="lores")
        print("Live stream started → rtsp://127.0.0.1:8554/cam")

    def stop(self):
        self.camera.stop_encoder(self.lores_encoder)
        self.camera.stop_preview()
        self.camera.stop()

    def get_camera(self):
        return self.camera
V
