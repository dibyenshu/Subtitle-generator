# Subtitle-generator
Generates the subtitles file(.srt) for a video using google speech api

Install the following before getting started:<br />
  1.Install python 3.6<br />
  2.Install ffmpeg (provides free CLI for multimedia editing)<br />
  3.Install google cloud services<br />

Steps/Instructions:
  1.Copy all the scripts to the windows directory G:\SIH\
  2.Rename the video that you want to get the subtitle of to "test" (without quotes) and put it in the folder
  3.Make a google cloud services acount with subscription and a storage with bucket name <urname>
  4.a.Edit the "call_trans.py" and replace "gs://sih2018/audio.flac" with "gs://<urname>/audio.flac"
    b.Edit the "up.py" and replace "gs://sih2018" with "gs://<urname>"
