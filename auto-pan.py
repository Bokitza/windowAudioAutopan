from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import math
from time import sleep

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

num = 0

while True:
    sleep(0.1)

    left = abs(math.sin(math.radians(num)))
    set_volume_left = -50 + left * 50

    right = abs(math.sin(math.radians(num + 90)))
    set_volume_right = -50 + right * 50

    volume.SetChannelVolumeLevel(1, set_volume_left, IAudioEndpointVolume._iid_)
    volume.SetChannelVolumeLevel(0, set_volume_right, IAudioEndpointVolume._iid_)

    num += 1