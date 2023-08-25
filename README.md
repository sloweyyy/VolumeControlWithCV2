# Hand Gesture Volume Control 12

Use hand gestures detected with MediaPipe to control your system volume.

## How It Works

The program uses MediaPipe to detect hand landmarks and determine finger positions. It tracks the index and middle finger tips to calculate the distance between them. This distance maps to the system volume level.

Finger counting is also used to mute/unmute based on a 3 finger gesture.

## Usage

1. Clone this repo
2. Run `pip install -r requirements.txt` 
3. Run `python main.py`
4. The webcam will open - move your index and middle fingers closer together to increase volume, further apart to decrease
5. Make a 3 finger gesture to mute, release to unmute

## Demo

![Demo gif of hand gestures controlling volume](demo.gif)

## Future Improvements

- Add calibration for different hand sizes
- Smooth out volume changes  
- Export as standalone application
- Support for mobile via Camera/gyroscope

Let me know if you have any other questions!
