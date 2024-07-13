# r = start rec
# s =  stop rec
# q = quit rec
import cv2

class VideoRecorder:
    def __init__(self, output_file):
        self.output_file = output_file
        self.recording = False
        self.video_capture = cv2.VideoCapture(0)
        self.frame_width = int(self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = None

    def start_recording(self):
        self.out = cv2.VideoWriter(self.output_file, self.fourcc, 20.0, (self.frame_width, self.frame_height))
        self.recording = True

    def stop_recording(self):
        if self.recording:
            self.out.release()
            self.recording = False

    def record(self):
        while True:
            ret, frame = self.video_capture.read()
            if ret:
                if self.recording:
                    self.out.write(frame)
                    cv2.putText(frame, 'Recording...', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow('Video Recorder', frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('r'):  
                    self.start_recording()
                elif key == ord('s'): 
                    self.stop_recording()
                elif key == ord('q'):  
                    break
            else:
                break
        self.video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    output_file = 'recorded_video.avi' 
    video_recorder = VideoRecorder(output_file)
    video_recorder.record()
