import cv2
import mediapipe as mp

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# Open a video capture
cap = cv2.VideoCapture(0)  # Change to the file path or camera index as needed

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame
    results = face_mesh.process(rgb_frame)

    # Draw facial landmarks on the frame
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=mp.solutions.drawing_utils.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1),
                connection_drawing_spec=mp.solutions.drawing_utils.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1)
            )

    # Display the frame
    cv2.imshow("Face Mesh", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
