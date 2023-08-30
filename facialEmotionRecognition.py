import cv2
import mediapipe as mp
from IPython.display import Image, display
import numpy as np

# Khởi tạo OpenCV và mediapipe
cap = cv2.VideoCapture(0)
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
face_detection = mpFaceDetection.FaceDetection(min_detection_confidence=0.5)

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Phát hiện khuôn mặt
    results = face_detection.process(imgRGB)

    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = img.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

            # Vẽ hình chữ nhật quanh khuôn mặt
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)

            # Lấy tọa độ các điểm trên khuôn mặt
            landmarks = detection.location_data.relative_keypoints
            for id, lm in enumerate(landmarks):
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 0:  # Điểm trên mũi
                    cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
                elif id == 1:  # Điểm trên hệ thống lông mày trái
                    cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
                # Thêm các điểm khác tương tự cho các vùng khác trên khuôn mặt

    # Display the image using IPython.display
    img_with_annotations = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB for display
    display(Image(data=cv2.imencode('.jpg', img_with_annotations)[1].tobytes()))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
