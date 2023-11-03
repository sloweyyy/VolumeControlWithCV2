from ctypes import cast, POINTER
from math import hypot
import cv2
import mediapipe as mp
import numpy as np
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volMin, volMax = volume.GetVolumeRange()[:2]

fingerCount = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []
    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handlandmark.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

            fingerCount = 0
            if lmList != []:
                for id, lm in enumerate(handlandmark.landmark):
                    if id in [4, 8, 12, 16, 20]:
                        if lm.y < lmList[id - 2][2]:
                            fingerCount += 1

    if fingerCount == 3:
        volume.SetMute(1, None)  # Mute the volume
    else:
        volume.SetMute(0, None)  # Unmute the volume

    if lmList != []:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        length = hypot(x2 - x1, y2 - y1)

        vol = np.interp(length, [15, 220], [volMin, volMax])
        volume.SetMasterVolumeLevel(vol, None)

        # Hand range 15 - 220
        # Volume range -63.5 - 0.0

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
