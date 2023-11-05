import cv2
import mediapipe as mp
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Initially set finger count to 0 for each cap
        fingerCount = 0

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get hand index to check label (left or right)
                handIndex = results.multi_hand_landmarks.index(hand_landmarks)
                handLabel = results.multi_handedness[handIndex].classification[0].label

                # Set variable to keep landmarks positions (x and y)
                hand_landmarks = []

                # Fill list with x and y positions of each landmark
                for landmarks in hand_landmarks.landmark:
                    hand_landmarks.append([landmarks.x, landmarks.y])

                # Test conditions for each finger: Count is increased if finger is
                # considered raised.
                # Thumb: TIP x position must be greater or lower than IP x position,
                # depending on hand label.
                if handLabel == "Left" and hand_landmarks[4][0] > hand_landmarks[3][0]:
                    fingerCount = fingerCount+1
                elif handLabel == "Right" and hand_landmarks[4][0] < hand_landmarks[3][0]:
                    fingerCount = fingerCount+1

                # Other fingers: TIP y position must be lower than PIP y position,
                # as image origin is in the upper left corner.
                if hand_landmarks[8][1] < hand_landmarks[6][1]:       #Index finger
                    fingerCount = fingerCount+1
                if hand_landmarks[12][1] < hand_landmarks[10][1]:     #Middle finger
                    fingerCount = fingerCount+1
                if hand_landmarks[16][1] < hand_landmarks[14][1]:     #Ring finger
                    fingerCount = fingerCount+1
                if hand_landmarks[20][1] < hand_landmarks[18][1]:     #Pinky
                    fingerCount = fingerCount+1

        # Perform actions based on finger count
        if fingerCount == 3:
            # Implement your "next" action here
            pyautogui.press('nexttrack')
        elif fingerCount == 4:
            # Implement your "back" action here
            pyautogui.press('prevtrack')
        elif fingerCount == 5:
            # Implement your "pause" action here
            pyautogui.press('space')

        # Draw hand landmarks
        mp_drawing.draw_landmarks(
            image,
            results.multi_hand_landmarks[0],  # Sử dụng results.multi_hand_landmarks thay vì hand_landmarks
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

        # Display image
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()
