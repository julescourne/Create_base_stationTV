# STVD-NLP
 This repo provided the codes to extract the information from XML metata of TV channels in France.
 
# Pre-processing with XML
The first step is the Pre-processing xml text to extract all of the TV programs during from at 06:00 AM to 02:00 AM of a next day.

Input: the list of XML file with its names formatted yyyy-mm-dd_HHMMSS.xml

Ouput: The list of TV programs that provided for each day based on the name of the XML file.

For example: 
Input: The file 2022-01-01_100000.xml

Ouput: List of TV programs which its starts FROM at 06:00:00 01-01-2022 TO at 02:00:00 02-01-2022

Notes: Using SHA-1 hash function for robustness of TV titles.

# Trimming video based on the information that extracted.
Notes:
* Recorded videos duration is 20 hours long per file (i.e., from 06:00 to 02:00 of next day).

The formated video / audio file names: c[0-7]_yyyymmdd_[video-audio].mp4

* Using the FFmpeg library to extract the segments of videos.

Input: The information of video, the channel, the timestamping and the location of the original video.

The timestamp used the window size W = Left_size, Right_size in minutes.

Output: The segments that are extracted from original video.




