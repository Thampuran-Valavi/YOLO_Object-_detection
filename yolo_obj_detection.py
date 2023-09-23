from ultralytics import YOLO
import cv2

model= YOLO('yolov8l.pt')
result= model("cars(1).mp4",show=True)
cv2.waitKey(0)