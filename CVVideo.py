from ultralytics import YOLO
import cv2

# Load a model
model = YOLO('yolov8x-seg.pt')  # load an official model

# Open the video stream or file
cap = cv2.VideoCapture('/Users/jayeshpaluru/Downloads/Test/IMG_2053.MOV')

# Prepare the video writer if you want to save the output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/path/to/save/output.avi', fourcc, 20.0, (640,  480))

# Process the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Predict with the model on the current frame
    results = model(frame)

    # Draw bounding boxes on the frame
    for result in results:
        if result.boxes is not None:
            for box in result.boxes:
                cords = box.xyxy[0].tolist()
                cords = [round(x) for x in cords]
                cv2.rectangle(frame, (cords[0], cords[1]), (cords[2], cords[3]), (0, 255, 0), 2)
                class_id = result.names[box.cls[0].item()]
                conf = round(box.conf[0].item(), 2)
                cv2.putText(frame, f'{class_id}: {conf}', (cords[0], cords[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Save the frame to the output video
    out.write(frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
