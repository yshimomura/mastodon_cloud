# -*- coding: utf-8 -*-

from mastodon import Mastodon
import datetime
import webbrowser
import tkinter as tk

mastodon = Mastodon(
client_id="app_key.txt",
access_token="user_key.txt",
api_base_url="https://mstdn.jp"
)

def IN():
    Intime = datetime.datetime.now()
    f =open('time.txt', 'w')
    f.write('in {0:%H}:{0:%M}'.format(Intime))
    f.close()

def OUT():
    Outtime = datetime.datetime.now()
    f =open('time2.txt', 'w')
    f.write('out {0:%H}:{0:%M}'.format(Outtime))
    f.close()

def TOOT():
    now = datetime.datetime.now()

    f = open('time.txt', 'r')
    f1 = f.read()
    f.close()

    g = open('time2.txt', 'r')
    g1 = g.read()
    g.close()

    word = text.get(1.0,tk.END)

    mastodon.toot('{0:%Y}-{0:%m}-{0:%d}\n{1}\n{2}\n{3}'.format(now, f1, g1, word))
    url = "https://mstdn.jp/web/"
    webbrowser.open(url)


root = tk.Tk()
root.title('toot system')
text = tk.Text(width=50, height=15)
button1 = tk.Button(root, text='In', command=IN)
button2 = tk.Button(root, text='Out', command=OUT)
button3 = tk.Button(root, text='Toot!', command=TOOT)

button1.pack(fill='both')
button2.pack(fill='both')
button3.pack(fill='both')
text.pack()

root.mainloop()
