import cv2
import matplotlib.pyplot as plt

def draw_bounding_boxes(image_path, annotation_path):
    # Read the image
    image = cv2.imread(image_path)

    # Read the annotation file
    with open(annotation_path, 'r') as f:
        lines = f.readlines()

    # Parse the annotation file
    boxes = []
    for line in lines:
        class_id, x, y, width, height = map(float, line.strip().split())
        left = int((x - width / 2) * image.shape[1])
        top = int((y - height / 2) * image.shape[0])
        right = int((x + width / 2) * image.shape[1])
        bottom = int((y + height / 2) * image.shape[0])
        boxes.append((left, top, right, bottom))

    # Draw bounding boxes on the image
    for box in boxes:
        left, top, right, bottom = box
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the image with bounding boxes using Matplotlib
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
