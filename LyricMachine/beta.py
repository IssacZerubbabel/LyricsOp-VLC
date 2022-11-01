import lyricsgenius
import tkinter
import tkinter.messagebox
genius = lyricsgenius.Genius("Cr-OoK33ItX3W345rMIhX48Cb7ktuNMmtsBr5_IB_9RfPAX59XMHHDB39PsXTVZv")
titl = open("C:\\Users\\Issac\\AppData\\Roaming\\vlc\\np_title.txt")
artis = open("C:\\Users\\Issac\\AppData\\Roaming\\vlc\\np_artist.txt")
title=titl.read()
artist=artis.read()
print(artist,"-",title)
song = genius.search_song(title,artist).lyrics
print(song)
#tkinter.messagebox.showinfo("{artist}-{title} lyrics",  song).format(artist,title)
'''root = tkinter.Tk()
root.geometry('500x500')
root.title("{artist}-{title} lyrics").format(artist,title)
root.option_add('*Dialog.msg.font', 'Helvetica 12')'''
tkinter.messagebox.showinfo(message=song)

