from ultralytics import YOLO
import matplotlib.pyplot as plt

# Loading pretrained model
model = YOLO('best.pt')

# Run inference on the source
# Change the source to the source of webcam of running machine

result = model(source=0, show=True, conf=0.3, save=True)
