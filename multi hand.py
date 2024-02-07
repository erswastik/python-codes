import cv2
import mediapipe as mp

# Initialize MediaPipe Hands for multi-hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)

# Open a video capture
cap = cv2.VideoCapture(0)  # Change to the file path or camera index as needed

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame
    results = hands.process(rgb_frame)

    # Draw hand landmarks on the frame for each hand
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for idx, landmark in enumerate(hand_landmarks.landmark):
                h, w, _ = frame.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.putText(frame, str(idx), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    # Display the frame
    cv2.imshow("Multi-Hand Tracking", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
