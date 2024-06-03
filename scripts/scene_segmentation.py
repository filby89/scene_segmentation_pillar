from ultralytics import FastSAM


class SceneSegmenter:
    def __init__(self):
        self.model = FastSAM('./FastSAM-x.pt')


    def track(self, frame, verbose=False, persist=True):
        results = self.model.track(frame, stream=False, show=False, conf=0.8, iou=0.2, mode="track", persist=persist, device='cuda', verbose=verbose)
    
        return results
    
