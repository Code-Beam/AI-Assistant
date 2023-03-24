from cgitb import text
from tkinter import *
import os
from screen_recorder_sdk import screen_recorder

def start_recording():
    screen_recorder.enable_dev_log()
    params = screen_recorder.RecorderParams()
    screen_recorder.init_resources(params)
    screen_recorder.start_video_recording(os.path.join("video.mp4"),120,16000000,True)
    record_btn["state"] = "disabled"
    stop_btn["state"] = "normal"

def stop_recording():
    screen_recorder.stop_video_recording()
    screen_recorder.free_resources()
    record_btn["state"] = "normal"
    stop_btn["state"] = "disabled"

def open_folder():
    path = os.path.realpath(os.getcwd())
    os.startfile(path)

main = Tk()
main.title("Screen Recorder Application")
app_label = Label(main,text="Screen Recorder", font=("arial",26,"bold"),padx=16,pady=16)
app_label.grid(columnspan=3)

photo = PhotoImage(file=os.path.join(r"C:\Users\kirth.VIJAYHARRE\OneDrive\Documents\pythonproj\Vijay-Folder\Assistant\cmds\assets\record.png"))
photo_image = photo.subsample(8,8)
record_btn = Button(main,image=photo_image,command=start_recording)
record_btn.grid(row=1,column=0,pady=16)

photo = PhotoImage(file=os.path.join(r"C:\Users\kirth.VIJAYHARRE\OneDrive\Documents\pythonproj\Vijay-Folder\Assistant\cmds\assets\stop-button.png"))
photo_image_stop = photo.subsample(8,8)
stop_btn = Button(main,image=photo_image_stop,command=stop_recording)
stop_btn.grid(row=1,column=1,pady=16)

photo = PhotoImage(file=os.path.join(r"C:\Users\kirth.VIJAYHARRE\OneDrive\Documents\pythonproj\Vijay-Folder\Assistant\cmds\assets\folder.png"))
photo_image_folder = photo.subsample(8,8)
folder_btn = Button(main,image=photo_image_folder,command=open_folder)
folder_btn.grid(row=1,column=2,pady=16)

stop_btn["state"] = "disabled"
main.mainloop()