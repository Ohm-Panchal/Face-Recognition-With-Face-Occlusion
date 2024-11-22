from mtcnn import MTCNN
import numpy as np
import cv2

class detector_face_occlusion():
    def __init__(self):
        # Initialize MTCNN detector
        self.detector = MTCNN()

    def detect_face(self, image):
        # Convert the image from BGR (OpenCV format) to RGB (MTCNN format)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Detect faces in the image
        detections = self.detector.detect_faces(image_rgb)
        
        # Initialize list for storing bounding boxes
        list_box = []

        # Iterate through each detected face
        for detection in detections:
            # Get the bounding box coordinates
            x, y, width, height = detection['box']
            x1, y1 = x, y
            x2, y2 = x + width, y + height
            
            # Append the box as an array [x1, y1, x2, y2]
            box = np.array([x1, y1, x2, y2])
            list_box.append(box)
        
        # Convert list of boxes to a NumPy array
        if len(list_box) > 0:
            list_box = np.vstack(list_box)
        else:
            list_box = np.array([])  # Return an empty array if no faces are detected
        
        print('-----------------------------------------------')
        print(np.array(list_box))
        print('-----------------------------------------------')
        
        return np.array(list_box)  # Return as a NumPy array