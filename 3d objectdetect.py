import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_objectron = mp.solutions.objectron

cap = cv2.VideoCapture(0)

with mp_objectron.Objectron(static_image_mode=False,
                            max_num_objects=5,
                            min_detection_confidence=0.3,  # Adjust as needed
                            min_tracking_confidence=0.5) as objectron:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Convert the image to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the frame
        results = objectron.process(image_rgb)

        # Draw landmarks and axis on the image
        if results.detected_objects:
            for detected_object in results.detected_objects:
                mp_drawing.draw_landmarks(
                    image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
                mp_drawing.draw_axis(image, detected_object.rotation,
                                     detected_object.translation)

        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Objectron', cv2.flip(image, 1))

        if cv2.waitKey(5) & 0xFF == 27:  # Press 'Esc' to exit
            break

cap.release()
cv2.destroyAllWindows()
