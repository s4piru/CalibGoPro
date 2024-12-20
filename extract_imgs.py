import cv2

capture = cv2.VideoCapture("source_video.MP4")
fps = capture.get(cv2.CAP_PROP_FPS)
print("fps: ", fps)
# 2 images per second
cap_per_sec = int(fps/2)
count = 0

while True:
    ret, frame = capture.read()
    if not ret:
        break
    if count % cap_per_sec == 0:
        cv2.imwrite(f"calib_{int(count/cap_per_sec)}.png", frame)
    count += 1