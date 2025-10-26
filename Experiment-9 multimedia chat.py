import tkinter as tk
from tkinter import filedialog, scrolledtext
from PIL import Image, ImageTk
from playsound import playsound
import threading

def send_text():
    msg = text_entry.get()
    if msg:
        chat_box.insert(tk.END, f"You: {msg}\n")
        text_entry.delete(0, tk.END)

def send_image():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if path:
        chat_box.insert(tk.END, f"You sent an image: {path}\n")
        img = Image.open(path)
        img.thumbnail((100, 100))
        img_tk = ImageTk.PhotoImage(img)
        
        # Insert image into ScrolledText using window_create
        chat_box.insert(tk.END, "\n")
        chat_box.image_create(tk.END, image=img_tk)
        chat_box.insert(tk.END, "\n")
        
        # Keep reference to prevent garbage collection
        if not hasattr(chat_box, 'images'):
            chat_box.images = []
        chat_box.images.append(img_tk)
        
        chat_box.yview(tk.END)

def send_audio():
    path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if path:
        chat_box.insert(tk.END, f"You sent an audio message: {path}\n")
        threading.Thread(target=lambda: playsound(path)).start()

# GUI Setup
window = tk.Tk()
window.title("Multimedia Messaging App")
window.geometry("400x500")

chat_frame = tk.Frame(window)
chat_box = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=50, height=20)
chat_box.pack()
chat_frame.pack(pady=10)

text_entry = tk.Entry(window, width=30)
text_entry.pack(side=tk.LEFT, padx=5)

btn_text = tk.Button(window, text="Send Text", command=send_text)
btn_image = tk.Button(window, text="Send Image", command=send_image)
btn_audio = tk.Button(window, text="Send Audio", command=send_audio)

btn_text.pack(side=tk.LEFT)
btn_image.pack(side=tk.LEFT)
btn_audio.pack(side=tk.LEFT)

window.mainloop()
