# Subtitle-generator
Generates the subtitles file(.srt) for a video using google speech api

Install the following before getting started:
  1.Install python 3.6<br />
  2.Install ffmpeg (provides free CLI for multimedia editing)<br />
  3.Install google cloud services<br />

Steps/Instructions:
  1.Copy all the scripts to the windows directory "G:\SIH\"<br />
  2.Rename the video that you want to get the subtitle of to "test" (without quotes) and put it in the folder<br />
  3.Make a google cloud services acount with subscription and a storage with bucket name <urname><br />
  4.a.Edit the "call_trans.py" and replace "gs://sih2018/audio.flac" with "gs://<urname>/audio.flac"<br />
    b.Edit the "up.py" and replace "gs://sih2018" with "gs://<urname>"<br />
  5.Run the following command in windows command prompt "gcloud auth login" and verify the account attached to google cloud services<br />
  6.Run the python script "RUN_IT.py" and wait for the subtitles.srt to appear in the folder <br />
  (usually takes around half of the video time)<br />
  7.If you want to reuse it<br />
    1.delete audio.flac from the folder<br />
    2.delete subtitles.srt from the folder<br />
    3.delete from your google cloud services bucket the audio.flac audio file<br />
    4.Now you can use RUN_IT.py again<br />
