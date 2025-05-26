import cv2
import os

SAVE_DIR = "student_images"
os.makedirs(SAVE_DIR, exist_ok=True)

def capture_student_image(student_id):
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Press 's' to Save Image", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            img_path = os.path.join(SAVE_DIR, f"{student_id}.jpg")
            cv2.imwrite(img_path, frame)
            print(f"✅ Image saved: {img_path}")
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage
student_id = input("Enter Student ID: ")
capture_student_image(student_id)
