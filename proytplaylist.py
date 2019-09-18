# Script to convert YT playlist to list of works
#
# 1. Download (private) playlist from YT
# 2. run script:
#       python3 proyt.py SelectionsYouTube.html
#
#
# Output file contains list of works saved in YT playlist

import fileinput
import html
import re
VIDEO = 'span id="video-title"'
selections = []

print('Starting to process input file...')
for line in fileinput.input():
     if re.search(VIDEO, line):
         selections.append(line)
print('Created list of Selections')

fh = open('YouTube.txt', 'w')
for line in selections:
    start = line.find('title=')

    #Example data
    #...title="Caro Emerald - Quicksand (Lyric Video)">
    #   1234567                                      321
    work = line[start + 7:-3]
    printable = html.unescape(work)
    fh.write(printable + '\n')
print('finished writing works...')
