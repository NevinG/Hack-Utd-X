# YOLOv8x-cls
from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2

# Load a model
model = YOLO('yolov8x-seg.pt')  # load an official model


# Image path
image_path = '/Users/jayeshpaluru/Downloads/Test/Residential Interior Pics/a Residential Int 1.jpeg'

# Display the image before prediction
img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

# Predict with the model
results = model(image_path)  # predict on an image
print(results)

# Display the image after prediction with bounding boxes
for result in results:
    if result.boxes is not None:
        for box in result.boxes:
            cords = box.xyxy[0].tolist()
            cords = [round(x) for x in cords]
            cv2.rectangle(img, (cords[0], cords[1]), (cords[2], cords[3]), (0, 255, 0), 2)
            class_id = result.names[box.cls[0].item()]
            conf = round(box.conf[0].item(), 2)
            cv2.putText(img, f'{class_id}: {conf}', (cords[0], cords[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

plt.imshow(img)
plt.show()