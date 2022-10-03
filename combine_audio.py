
import sys
import moviepy.editor as mpy
from moviepy.editor import *

#image_width, image_height = 2160, 3840
#image_width, image_height = 1080, 1350 #instagram smaller hd
#image_width, image_height = 1080, 1920    #instagram larger hd
#image_width, image_height = 3840, 2160 #4k for youtube
#image_width, image_height = 2160, 3840 #4k vertical

def combine_audio(vidname, audname, outname): #, fps=30): #60): 
    #clip_length = None
    clip_length = 5 #int(clip_duration / 2)
    
    # loading video dsa gfg intro video
    clip = VideoFileClip(vidname)
    
    #https://ericgitonga.substack.com/p/processing-videos-with-moviepy-25b238302af6
    #mpy.ipython_display(clip, width=500, maxduration=clip_duration)
    clip_duration = clip.duration - 1
    print('clip_duration', clip_duration)
    mpy.ipython_display(clip, maxduration=(clip_duration))
    
    
    
    if clip_length != None:
        clip = clip.subclip(0, clip_length) # getting only first 5 seconds
    
    # https://moviepy.readthedocs.io/en/latest/ref/VideoClip/VideoClip.html
    if False:
        clip.resize( (image_width, image_height) ) # New resolution: (460,720)
        #myClip.resize(0.6) # width and height multiplied by 0.6
        #myClip.resize(width=800) # height computed automatically.
        #myClip.resize(lambda t : 1+0.02*t) # slow swelling of the clip


    # loading audio file
    audioclip = AudioFileClip(audname)
    if clip_length != None:
        audioclip = audioclip.subclip(0, clip_length) # getting only first 5 seconds

    # adding audio to the video clip
    videoclip = clip.set_audio(audioclip)

    # showing video clip
    videoclip.ipython_display()
    
    videoclip.write_videofile(outname) #,fps=fps)
    
    
    #import moviepy.editor as mpe
    #my_clip = mpe.VideoFileClip(vidname)
    #audio_background = mpe.AudioFileClip(audname)
    #final_clip = my_clip.set_audio(audio_background)
    #final_clip.write_videofile(outname,fps=fps)


#python combine_audio music_video.mp4 my_song.mp3 music_video_done.mp4
mp4 = sys.argv[1]
mp3 = sys.argv[2]
out = sys.argv[3]

print('......', mp4, mp3, out)
combine_audio(mp4, mp3, out) # i create a new file