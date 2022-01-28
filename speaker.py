

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)


volume = cast(interface, POINTER(IAudioEndpointVolume))

def mute():
    volume.SetMute(1, None)

def unmute():
    volume.SetMute(0, None)


