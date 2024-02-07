import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        continue

    # Flip the frame horizontally for selfie view, and convert the BGR image to RGB.
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands.
    results = hands.process(frame)

    # Draw hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the coordinates of the index fingertip (landmark 8)
            x, y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x, hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y

            # Convert the coordinates to pixel space
            screen_width, screen_height = pyautogui.size()
            x_pixel, y_pixel = int(x * screen_width), int(y * screen_height)

            # Move the mouse pointer to the index fingertip position
            pyautogui.moveTo(x_pixel, y_pixel)

            # Click left mouse button if index fingertip is above landmark 5 (base of index finger)
            if hand_landmarks.landmark[6].y < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y < hand_landmarks.landmark[5].y:
                pyautogui.click()
            elif hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y < hand_landmarks.landmark[6].y:
                pyautogui.mouseDown()
            else :
                pyautogui.mouseUp()  # Press the left click
            
    # Convert the BGR image back to BGR for rendering
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Display the frame
    cv2.imshow('Hand Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()
