import cv2
import mediapipe as mp
from ctypes import WinDLL

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.6)

# Windows volume control
user32 = WinDLL("user32")

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

    # Count fingers and control volume (example)
    if results.multi_hand_landmarks:
        # Get landmarks
        landmarks = results.multi_hand_landmarks[0].landmark

        # Check which fingers are extended
        extended_fingers = [i for i in [4, 8, 12, 16, 20] if landmarks[i].y < landmarks[5].y]

        # Count fingers based on landmark positions (example)
        fingers = len(extended_fingers)

        # Display the number of extended fingers and their landmark numbers on the screen
        cv2.putText(frame, f'Extended fingers: {fingers}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, f'Landmarks: {extended_fingers}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Control volume based on number of fingers detected (example)
        if fingers == 5:  # If five fingers are detected
            for _ in range(50):  # Turns volume up:
                user32.keybd_event(0xAF, 0, 0, 0)
                user32.keybd_event(0xAF, 0, 2, 0)
        elif fingers == 1:  # If one finger is detected
            for _ in range(50):  # Turns volume down:
                user32.keybd_event(0xAE, 0, 0, 0)
                user32.keybd_event(0xAE, 0, 2, 0)

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
