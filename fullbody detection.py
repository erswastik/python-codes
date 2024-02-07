import cv2
import mediapipe as mp

# Initialize MediaPipe Holistic
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic()

# Open a video capture
cap = cv2.VideoCapture(0)  # Change to the file path or camera index as needed

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Holistic
    results = holistic.process(rgb_frame)

    # Draw holistic landmarks on the frame
    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(
            frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

    if results.left_hand_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(
            frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

    if results.right_hand_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(
            frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

    # Display the frame
    cv2.imshow("Holistic with Pose and Hand Landmarks", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
