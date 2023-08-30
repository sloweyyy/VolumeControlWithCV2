# Volume Control and Facial Expression Recognition with OpenCV and MediaPipe

This repository contains Python scripts that demonstrate how to control the system volume based on hand gestures and perform facial expression recognition using OpenCV and MediaPipe libraries.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Scripts](#scripts)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project showcases the use of OpenCV and MediaPipe libraries to perform two main tasks:

1. **Volume Control using Hand Gestures**: The first script (`volume_control_hand_gestures.py`) demonstrates how to control the system volume by interpreting specific hand gestures using the MediaPipe Hands module.

2. **Facial Expression Recognition**: The second script (`facial_expression_recognition.py`) illustrates how to detect and recognize facial expressions in real-time using the MediaPipe Face Detection module.

# Installation

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- pycaw
- comtypes
- keyboard (for the third script)

You can install the required libraries using the following command:
```
pip install opencv-python mediapipe pycaw comtypes keyboard
```

## Clone Repository
1. Clone this repository to your local machine:
```
git clone https://github.com/sloweyyy/VolumeControlWithCV2.git
```
2. Navigate to the repository directory:
```
cd VolumeControlWithCV2
```
Run the desired script using Python.

# Usage
1. Run the scripts as described in the Installation section.
2. Follow the on-screen instructions for each script.
3. For the volume control script, use hand gestures to control the system volume.
4. For the facial expression recognition script, observe the real-time detection of facial expressions.

## Scripts

- `volume_control_hand_gestures.py`: Control the system volume using hand gestures detected by the MediaPipe Hands module.

- `facial_expression_recognition.py`: Detect and recognize facial expressions in real-time using the MediaPipe Face Detection module.

- `combined_volume_and_expression.py`: Combines both volume control and facial expression recognition functionalities.

## Contributing

Contributions are welcome! If you find any issues or have improvements to suggest, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
