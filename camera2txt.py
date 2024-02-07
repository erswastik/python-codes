import cv2
import pytesseract

# Set the path to the Tesseract OCR executable (change this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def capture_and_recognize_text():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to grayscale for better OCR accuracy
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform text recognition using Tesseract OCR
        text = pytesseract.image_to_string(gray)

        # Display the original frame and recognized text
        cv2.imshow('Webcam', frame)
        print('Recognized Text:', text)

        # Break the loop if the 'Esc' key is pressed
        if cv2.waitKey(1) == 27:
            break

    # Release the webcam and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_recognize_text()
