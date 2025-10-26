import cv2
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import time
import os

# ---- Audio: record a short WAV first ----
def record_audio_wav(filename="output.wav", seconds=5, samplerate=44100, channels=1):
    print(f"Recording audio for {seconds} s...")
    audio = sd.rec(int(seconds * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
    sd.wait()
    write(filename, samplerate, audio)
    print(f"Saved audio: {filename}")

# ---- Camera: live preview, still image capture, optional video recording ----
def camera_session(image_name="captured_image.png", video_name="output.mp4", fps=20.0, cam_index=0):
    cam = cv2.VideoCapture(cam_index)
    if not cam.isOpened():
        raise RuntimeError("Cannot open camera")

    width  = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = None
    recording = False
    frames = 0

    print("Camera ready: press 's' to save image, 'r' to start/stop video, 'q' to quit.")
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Camera read failed; exiting.")
            break

        if recording:
            writer.write(frame)
            frames += 1
            cv2.putText(frame, "REC", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 2)

        cv2.imshow("Camera", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            cv2.imwrite(image_name, frame)
            print(f"Saved image: {image_name}")

        elif key == ord('r'):
            if not recording:
                writer = cv2.VideoWriter(video_name, fourcc, fps, (width, height))
                if not writer.isOpened():
                    print("Failed to open video writer.")
                else:
                    recording = True
                    frames = 0
                    print(f"Recording video to {video_name} ... press 'r' again to stop.")
            else:
                recording = False
                if writer is not None:
                    writer.release()
                    writer = None
                print(f"Stopped recording. Frames saved: {frames}")

        elif key == ord('q'):
            break

    if recording and writer is not None:
        writer.release()
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 1) Record mic audio (WAV)
    record_audio_wav(filename="output.wav", seconds=5, samplerate=44100, channels=1)

    # 2) Open camera window: 's' to save still, 'r' to start/stop video, 'q' to quit
    camera_session(image_name="captured_image.png", video_name="output.mp4", fps=20.0, cam_index=0)
