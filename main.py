import os
import cv2
import time
import random
import numpy as np
import platform
import subprocess
import sounddevice as sd
import pyttsx3
import matplotlib.pyplot as plt
from colorama import Fore, Style
from matplotlib.animation import FuncAnimation

CHARS = np.array(list(" .:-=+*#%@"))
FPS = 30
WIDTH = 200
VIDEO_PATH = "skull.mp4"
MUTATION_RATE = 0.03

engine = pyttsx3.init()
