from ultralytics import YOLO

model = YOLO("boxing_test/last_box.pt")  # ton modèle


# results = model.predict(source="boxing_test/photo.png", imgsz=640, conf=0.35)  # ou "input.mp4"

# for r in results:
#     # classes prédites pour chaque personne
#     cls_ids = r.boxes.cls.cpu().numpy()          # indices de classes
#     confs   = r.boxes.conf.cpu().numpy()         # confiances
#     # keypoints (N, K, 2): x,y (ou .xyn pour normalisés)
#     kpts    = r.keypoints.xy.cpu().numpy()

#     # mapping id->nom:
#     names = model.names  # dict {id: 'Hook-Punch', ...}
#     labels = [names[int(i)] for i in cls_ids]
#     print(list(zip(labels, confs)))



# Predict on a video file; writes an annotated MP4 under runs/pose/predict*
results = model.predict(
    source="boxing_test/cross_013.mp4",  # or 0 for webcam
    imgsz=640,
    conf=0.35,
    save=True,       # save annotated video
    vid_stride=1     # process every frame; increase (e.g., 2/3) to go faster
)