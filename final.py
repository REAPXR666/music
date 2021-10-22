from __future__ import unicode_literals
from bs4 import BeautifulSoup
from gtts import gTTS
import requests
import os,sys
import time
import urllib
import urllib.request
import re
from pytube import YouTube
import youtube_dl
from youtube_search import YoutubeSearch
import time
import subprocess
#main selection menu
print("""
                            
                               | MAIN MENU |                                   
                           
IMAGES:                       TEXT:                  PLAYERS:
1) image downloader       5) text to speech     7) music player
                                                 
AUDIO:                        OTHER:                 
2) youtube to audio         6) mp3 converter (in progress)      
3) spotify downloader
4) bass booster
""")
time.sleep(0.5)
print("""
GET MORE FEATURES:

DOWNLOADS:
faster speeds
soundcloud to mp3
youtube channel scraper
video downloads

""")
time.sleep(1)

print("Checking entered key")
time.sleep(1)
with open('Licence.txt') as f:
    contents = f.read()
    print(contents)
key = contents
time.sleep(2)
if key == "VACERHc6Wk":
    print("Succesfully activated PRO acc")
    time.sleep(2)
    print("BONUS FEATURES")
    time.sleep(1)
    print("""

            DLC
8: Soundcloud to mp3
9. Speech to text
""")
else:
    print("Invalid Key")
    
time.sleep(1)
choice = int(input("Please select an option: "))

if choice == 1:
    tag = input("please enter the image idea you want: ")
    form = input("What file format are you looking for: ")
    am = int(input("How many images do you want: "))
    with open('search_filter.txt', 'a') as f:
        f.write(tag)
        f.write('\n')
    #Enter your search URL here (Remove the placeholder first). Get this from just searching like normal on 4walled.cc and copying the URL.
    url = "http://www.wallpaperswide.com"
    #Enter your download path here (This will download to a new folder, wallpapers, in the directory this script is ran from)
    path = "images//"
    #Pages of wallpapers to download (30 per page)
    limit = am

    resultsurl = url.replace("/sarch.php", "/result.php") + "/"+tag+"-wallpapers/page/"
    if not os.path.exists(path): os.makedirs(path)
    print (resultsurl)


    for i in range(0, limit):
        pages = i * 1
        imagepageurl = resultsurl + str(pages)
        print (imagepageurl)
        r = requests.get(imagepageurl)
        print (r)
        html = r.text
    
        soup = BeautifulSoup(html)    
    
        for tag in soup.find_all("img"):
            thumburl = tag['src']
            #print thumburl
            realurl1 = thumburl.replace("/thumbs", "/download")
            print (realurl1)
            realurl = realurl1.replace("-t1", "-wallpaper-1920x1080")
            print (realurl)
            with open('LOGS.txt', 'a') as f:
                f.write(realurl)
                f.write('\n')
        
            try:
                r = requests.get(realurl)
                r.raise_for_status()            
            except:
                realurl = realurl.replace("jpg")
            
        
            fr = requests.get(realurl)
            #filepath = path + realurl
            #with open(filepath, 'wb') as writer:
            #writer.write(fr.content)
            #fr.close()
            print ("Downloading " + realurl)
        
            imageFile = open(os.path.join('images', os.path.basename(realurl)), 'ab')
            for chunk in fr.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

elif choice == 2:
    import youtube_dl
    print("Insert the link")
    link = input ("")
    if  "youtube.com" not in link:
        print("Invalid link")
        time.sleep(100000000)
    else:
          print("Found link")
         

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


elif choice == 3:
    lenk = input("please enter song url: ")

    if lenk.find('https://open.spotify.com') != 1:
        try:    
            res = requests.get(lenk)
            soup = BeautifulSoup(res.text,'lxml')
            title = soup.find('meta', property='og:title')
            artist_link = soup.find('meta', property="music:musician")['content']
            artist_page = BeautifulSoup(requests.get(artist_link).text,'lxml')
            artist_name = artist_page.find('meta', property='og:title')
            song = title['content']
            artist =  artist_name['content']
            song_name = str(song + " " + artist) 
            print( "Song Found :  " +  song, "by: " + artist)

            song_name_final = song_name.replace(" ", "+")
            pre_url = "https://www.youtube.com/results?search_query="
            yt_search = pre_url + song_name_final
            print(yt_search)

            results = list(YoutubeSearch(str(song_name), max_results=1).to_dict())[-1]
            # results2 = list(results)[-1]

            # print(type(results))

            results2 = str(results['url_suffix'])
            print(results2)
        
            print("Song Found")
            yt_pre = str("https://www.youtube.com/" + results2)
            print(yt_pre)
            print("Starting download...")
            # os.system('cmd /c "python mp3.py "')

            # youtube_dl.YoutubeDL(yt_pre)

            # checks if the required 'youtube-dl' package is available
            def check():
                import importlib
                try:                            # CHECKS if AVAILABLE
                    importlib.import_module('youtube_dl')

                except ModuleNotFoundError:     # if NOT AVAILABLE --> then installs 'youtube-dl' python package
                    print('youtube-dl NOT FOUND in this Computer !')
                    print('The SCRIPT will install youtube-dl python package . . .')
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'youtube-dl'])

                finally:                        # if AVAILABLE --> then proceeds with downloading the music
                    globals()['youtube_dl'] = importlib.import_module('youtube_dl')
                    run()




            # Returns the default downloads path for linux or windows
            def get_download_path():
                if os.name == 'nt':         # for WINDOWS system
                    import winreg
                    sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
                    downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                        location = winreg.QueryValueEx(key, downloads_guid)[0]
                    return location
                else:                       # for LINUX & MAC
                    return os.path.join(os.path.expanduser('~'), 'downloads')






            # gets ./ffmpeg.exe PATH 
            ffmpeg_path = os.getcwd()

            set_path = input("please enter file location to save to: ")
            '''sets DEFALUT PATH for download Location'''
            path = set_path

            ''' add a CUSTOM PATH for download loaction (remove '#' from the line BELOW & add the new PATH inside ' '(quotes) '''
            #path = ''
        
            # Main Download Script For Audio
            def run():
                options = {
                    # PERMANENT options
                    'format': 'bestaudio/best',
                    'ffmpeg_location': f'{ffmpeg_path}/ffmpeg.exe',
                    'keepvideo': False,
                    'outtmpl': f'{path}/%(title)s.*',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '320'
                    }],

                    #(OPTIONAL options)
                    'noplaylist': True
                }

                # the 'youtube_dl' module will be imported on program run
                with youtube_dl.YoutubeDL(options) as mp3:
                    mp3.download([yt_pre])
                    print("Download Completed!")




            # runs Main Download Script


      
            
        except:
            print("Enter valid url")        
                
    if __name__ == '__main__':
        check()

elif choice == 4:
    from pydub import AudioSegment
    from os import listdir
    import numpy as np
    import math
    print("2 DB is highly recommended")
    boost = input("how many db do you want to boost by? ")
    print("NOW BASS BOOSTING... this may take a minuit")
    song_dir = "songs"
    attenuate_db = 0
    accentuate_db = boost


    def bass_line_freq(track):

        sample_track = list(track)

        # c-value
        est_mean = np.mean(sample_track)

        # a-value
        est_std = 3 * np.std(sample_track) / (math.sqrt(2))

        bass_factor = int(round((est_std - est_mean) * 0.005))

              
        return bass_factor

    for filename in listdir(song_dir):
        sample = AudioSegment.from_mp3(song_dir + "/" + filename)
        filtered = sample.low_pass_filter(bass_line_freq(sample.get_array_of_samples()))
        print("boosted: " + filename)
        combined = (sample - attenuate_db).overlay(filtered + accentuate_db)
        combined.export("boosted/" + filename.replace(".mp3", "") + " - bass boosted " + boost + " db.mp3", format="mp3")
    print("your song/s have been bass boosted by", boost, "db")

elif choice == 5:
    mytext = input("what do you want to say: ")
    print("""{'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic',
'hy': 'Armenian', 'bn': 'Bengali', 'bs': 'Bosnian', 'ca': 'Catalan',
'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch',
'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino',
'fi': 'Finnish', 'fr': 'French', 'de': 'German', 'el': 'Greek',
'gu': 'Gujarati', 'hi': 'Hindi', 'hu': 'Hungarian', 'is': 'Icelandic',
'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese',
'kn': 'Kannada', 'km': 'Khmer', 'ko': 'Korean', 'la': 'Latin', 'lv':
'Latvian', 'mk': 'Macedonian', 'ml': 'Malayalam', 'mr': 'en': english""")
    
    language = input("what language? ")
    myobj = gTTS(text=mytext, lang=language, slow=False)
    fname = input("what do you want the file to be called: ")
    output = fname + ".mp3"
    myobj.save(fname + ".mp3")
    select = input("\n\tyes: play output \n\tno) dont play output \n\t")
    if select == "yes":
        os.system(output)
        
    else:
        print("you selected NO")
        time.sleep(2)
    print("your file: " + output, "was succesfully created")
    

elif choice == 6:
    print("NOTE: THIS REQUIRES ADMIN PERMISSIONS")
    time.sleep(1)
    from pydub import AudioSegment
    print("PLEASE ADD FULL FILE DIRECTORY")
    directoryin = input()
    print("Where do you want to save to")
    directoryout = input()
    sound = AudioSegment.from_mp3(directoryin)
    sound.export(directoryout, format="wav")

elif choice == 7:
    from tkinter import *
    import pygame
    import os

    # Defining MusicPlayer Class
    class MusicPlayer:

      # Defining Constructor
      def __init__(self,root):
        self.root = root
        # Title of the window
        self.root.title("Music Player")
        # Window Geometry
        self.root.geometry("1000x200+200+200")
        # Initiating Pygame
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()

        # Creating Track Frame for Song label & status label
        trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        trackframe.place(x=0,y=0,width=600,height=100)
        # Inserting Song Track Label
        songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Status Label
        trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=1,padx=10,pady=5)

        # Creating Button Frame
        buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        buttonframe.place(x=0,y=100,width=600,height=100)
        # Inserting Play Button
        playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Pause Button
        playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=1,padx=10,pady=5)
        # Inserting Unpause Button
        playbtn = Button(buttonframe,text="RESUME",command=self.unpausesong,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=2,padx=10,pady=5)
        # Inserting Stop Button
        playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=3,padx=10,pady=5)

        # Creating Playlist Frame
        songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        songsframe.place(x=600,y=0,width=400,height=200)
        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe,orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs
        os.chdir = input("please enter music file directory")
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
          self.playlist.insert(END,track)

      # Defining Play Song Function
      def playsong(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()

      def stopsong(self):
        # Displaying Status
        self.status.set("-Stopped")
        # Stopped Song
        pygame.mixer.music.stop()

      def pausesong(self):
        # Displaying Status
        self.status.set("-Paused")
        # Paused Song
        pygame.mixer.music.pause()

      def unpausesong(self):
        # Displaying Status
        self.status.set("-Playing")
        # Playing back Song
        pygame.mixer.music.unpause()

    # Creating TK Container
    root = Tk()
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
    # Root Window Looping
    root.mainloop()

#########################
#DLC#
#########################
elif choice == 8:
    import youtube_dl
    print("Insert the link")
    link = input ("")

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

elif choice == 9:
    import speech_recognition as sr

    r = sr.Recognizer()

    audio = str(input("Please enter file name + extention: "))

    with sr.AudioFile(audio) as source:
        audio = r.record(source)
        print ('Converting...')

    try:
        text = r.recognize_google(audio)
        print (text)
        with open('Speech convert.txt', 'a') as f:
            f.write(text)
            f.write('\n \n IGNORE \n \n')
    except Exception as e:
        print (e)





print("How would you rate our service")
time.sleep(1)
rate = input("Please enter what you think about our service: ")
print("Thank you for rating us!")
time.sleep(10)
