from ultralytics import FastSAM


class SceneSegmenter:
    def __init__(self):
        self.model = FastSAM('./FastSAM-s.pt')


    def track(self, frame, verbose=False, persist=True):
        results = self.model.track(frame, stream=False, show=False, conf=0.4, iou=0.2, mode="track", persist=persist, device='cpu', verbose=verbose,
                                   save=True)
    
        return results
    
