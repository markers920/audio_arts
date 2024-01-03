
#may need to: 
# conda install -c conda-forge ffmpeg
#

from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import sys
import time
import random

def main():
    input_dir = sys.argv[1]
    output_name = sys.argv[2]
    mute_audio = True if len(sys.argv) < 4 else bool(sys.argv[3])
    
    time_start = time.process_time()

    print('input_dir:', input_dir)
    print('output_name:', output_name)
    print('mute_audio:', mute_audio)

    files = sorted(os.listdir(input_dir))

    video_clips = []
    for file in files:
        input_path = os.path.join(input_dir, file)
        
        # skip directories
        if os.path.isdir(input_path):
            continue
            
        print(input_path)
        single_clip = VideoFileClip(input_path)
        video_clips.append(single_clip)
        
    final_clip = concatenate_videoclips(video_clips)
    if mute_audio:
        final_clip = final_clip.without_audio()
        
    final_clip.write_videofile(output_name)
    
    time_end = time.process_time()
    
    print('process time:', time_end-time_start)
    
    
if __name__ == '__main__':
    print('#'*80)
    print('usage:', '\n', 'python concatenate_video_files.py <input_dir> <output_name> <mute_audio=True>')
    print('#'*80, flush=True)
    main()