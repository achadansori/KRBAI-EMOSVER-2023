import cv2
import numpy as np

def detect_ball_color(frame, lower_color, upper_color):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    ball_detected = False
    ball_center = None

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            moment = cv2.moments(contour)
            if moment["m00"] != 0:
                ball_center = (int(moment["m10"] / moment["m00"]), int(moment["m01"] / moment["m00"]))
                ball_detected = True
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                cv2.circle(frame, ball_center, 5, (0, 255, 0), -1)
                break
    
    return ball_detected, ball_center

cap = cv2.VideoCapture(0)  # Change device number if needed

cv2.namedWindow('Lane Detection')

# Trackbars for color thresholds
cv2.createTrackbar('H Min (Red)', 'Lane Detection', 0, 180, lambda x: None)
cv2.createTrackbar('H Max (Red)', 'Lane Detection', 10, 180, lambda x: None)
cv2.createTrackbar('H Min (Green)', 'Lane Detection', 35, 180, lambda x: None)
cv2.createTrackbar('H Max (Green)', 'Lane Detection', 85, 180, lambda x: None)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get trackbar values for color thresholds
    red_lower = np.array([cv2.getTrackbarPos('H Min (Red)', 'Lane Detection'), 100, 100])
    red_upper = np.array([cv2.getTrackbarPos('H Max (Red)', 'Lane Detection'), 255, 255])
    green_lower = np.array([cv2.getTrackbarPos('H Min (Green)', 'Lane Detection'), 100, 100])
    green_upper = np.array([cv2.getTrackbarPos('H Max (Green)', 'Lane Detection'), 255, 255])

    red_detected, red_center = detect_ball_color(frame, red_lower, red_upper)
    green_detected, green_center = detect_ball_color(frame, green_lower, green_upper)

    if red_detected and green_detected:
        cv2.line(frame, red_center, green_center, (0, 0, 255), 2)

        if red_center[0] < green_center[0]:
            cv2.putText(frame, 'Kiri', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif red_center[0] > green_center[0]:
            cv2.putText(frame, 'Kanan', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Lane Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
