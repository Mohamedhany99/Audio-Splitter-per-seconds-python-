# -*- coding: utf-8 -*-
"""
Created on Sat May  2 01:04:00 2020

@author: Mohamed Hany
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:01:46 2020

@author: aa
"""
from pydub import AudioSegment
import wave

t1=0
t2=3000
filenme="NA.wav"
wavfile = wave.open(filenme)
frames = wavfile.getnframes()
rate = wavfile.getframerate()
duration = frames/float(rate)
print(duration)
for i in range(int(duration)):
    newAudio = AudioSegment.from_wav("NA.wav")
    newAudio = newAudio[t1:t2]
    newaudname="NA"+str(i)+".wav"
    newAudio.export(newaudname, format="wav") #Exports to a wav file in the current path.
    
    t1 = t2     #Works in milliseconds
    t2 = t2 + 3000
    seconds = t2/1000
    print(seconds)
    if seconds>duration:
        break;
