import cv2
from ultralytics import YOLO

model = YOLO("boxing_test/last_box.pt")
names = model.names

cap = cv2.VideoCapture(0)           
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

for results in model.predict(source=0, stream=True, conf=0.35, imgsz=640, verbose=False):
    frame = results.orig_img
    annotated = results.plot()      

    # Example: read classes & confidences
    if results.boxes is not None and len(results.boxes) > 0:
        cls_ids = results.boxes.cls.cpu().numpy()
        confs   = results.boxes.conf.cpu().numpy()
        labels  = [names[int(i)] for i in cls_ids]
        # keypoints: (N, K, 2)
        kpts    = results.keypoints.xy.cpu().numpy() if results.keypoints is not None else None
        # do something with labels/confs/kpts here

    cv2.imshow("PunchDetector Live", annotated)
    if cv2.waitKey(1) & 0xFF in (ord('q'), 27):  # q or Esc
        break

cap.release()
cv2.destroyAllWindows()