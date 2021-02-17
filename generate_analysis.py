import os

own_dir = os.path.dirname(__file__)
path = "test_videos"
# python detect.py --source test_videos/ank2.mp4 --weights weights/yolov5m.pt --conf 0.6 --classes 0 8
weights = ["yolov5s.pt", "yolov5m.pt", "yolov5l.pt", "yolov5x.pt"]
conf = ["0.6", "0.7", "0.8", "0.9"]
for w in weights:
    for c in conf:
        for f in os.listdir(path):
            os.system(
                "python detect.py --source test_videos/"
                + f
                + " --weights weights/"
                + w
                + " --conf "
                + c
                + " --classes 0 8"
            )
