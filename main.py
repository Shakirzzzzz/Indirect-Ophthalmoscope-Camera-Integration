from picamera2.encoders import H264Encoder
from picamera2 import Picamera2
import time

picam2 = Picamera2()
encoder = H264Encoder(bitrate=1000000)
