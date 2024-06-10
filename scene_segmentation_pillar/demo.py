import os
import cv2
from scene_segmentation import SceneSegmenter


scenesegmenter = SceneSegmenter()

video = cv2.VideoCapture('samples/test_video.mp4')

video_out = cv2.VideoWriter('samples/test_video_out.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (int(video.get(3)), int(video.get(4))))

while True:
    ret, frame = video.read() 

    if not ret:
        break

    results = scenesegmenter.track(frame, verbose=False)
    im = results[0].plot() 

    video_out.write(im)

    for result in results:
        print(result.boxes)

video.release()