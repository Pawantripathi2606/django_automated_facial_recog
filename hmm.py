import cv2
import numpy as np

clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.xml")

dummy_img = np.zeros((100,100), dtype=np.uint8)  # black dummy image

try:
    id, confidence = clf.predict(dummy_img)
    print("Classifier has data ✅ | Sample prediction:", id, confidence)
except Exception as e:
    print("Classifier failed ❌:", e)
