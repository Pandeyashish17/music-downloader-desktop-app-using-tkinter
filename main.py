from pytube import YouTube
from tkinter import * 
import os

root = Tk()
root.geometry('800x800')
root.title('Download Youtube Music')
root.config(bg='#add8e6')

try:
    def func(default=''):
        def Download():
            out_file = video.download(output_path='.')

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            d=Label(text='Download Completed!!', font=('Roboto',20,'normal'), fg='#000000', bg='#add8e6') 
            d.place(relx=0.5, rely=0.375, anchor=CENTER)

            
        url=UrlOfYoutubeVideo.get()
        
        try:
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            
            
        except:
            l=Label(text='Please Enter a valid Url', font=('Roboto',20,'normal'), fg='#000000', bg='#add8e6') 
            l.place(relx=0.5, rely=0.375, anchor=CENTER)
            
        else:
            
            D_button = Button(root, text='Download',font=('Roboto',20,'normal'),command=Download, bg='#000000', fg='#add8e6')
            D_button.place(relx=0.5, rely=0.375, anchor=CENTER)
except:
    print('Error Occured')    



Screen = Label(text='Youtube Video Downloader', fg='#000000', bg='#add8e6', font=('Roboto',28,'bold'),width=22)
Screen.place(relx=0.5, rely=0.155, anchor=CENTER)

UrlOfYoutubeVideo = Entry(width = 20, borderwidth=3, font=('Roboto',16,'normal'), justify=CENTER, bg='#ffffff',fg='#000000')
UrlOfYoutubeVideo.insert(0, 'Enter URL of the Youtube Video')

UrlOfYoutubeVideo.place(relx=0.5, rely=0.275, anchor=CENTER)

enter = Button(root, text='Enter', fg='#add8e6', bg='#000000', font=('Roboto',16,'normal'), command=func)
enter.place(relx=0.7, rely=0.275, anchor=CENTER)

root.bind('<Return>',func)

root.mainloop()