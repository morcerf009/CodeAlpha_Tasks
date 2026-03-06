import cv2
from ultralytics import YOLO

def main():
    # Initialize the YOLOv8 model
    model = YOLO("yolov8n.pt")

    # Access the default camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'q' to exit.")

    # Create a full-screen window
    cv2.namedWindow("Real-Time Object Detection & Tracking", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Real-Time Object Detection & Tracking", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Perform tracking on the current frame
        results = model.track(frame, persist=True)

        # Plot the results on the frame
        annotated_frame = results[0].plot()

        # Display the output
        cv2.imshow("Real-Time Object Detection & Tracking", annotated_frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Clean up resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
