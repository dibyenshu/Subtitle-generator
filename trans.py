#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import argparse
import io

def min(seconds):#returns string 00:00:00,000
    if(seconds<10):
	    return '00:00:0' + str(seconds) + ',000'
    elif(seconds<60):
        return '00:00:' + str(seconds) + ',000'
    elif(seconds//60<10):
        return '00:0' + str(seconds//60) + ':' + str(seconds%60) + ',000'
    else:
        return '00:' + str(seconds//60) + ':' + str(seconds%60) + ',000'

# [START def_transcribe_gcs]
def transcribe_gcs_with_word_time_offsets(gcs_uri):
    """Transcribe the given audio file asynchronously and output the word time
    offsets."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US',
        enable_word_time_offsets=True)

    operation = client.long_running_recognize(config, audio)

    print('Currently transcribing on google server.. \nPlease wait until it is complete.\n Generally takes half of video time')
    result = operation.result(timeout=250)

    count = 1
    caption = ''
    st_time = 0
    en_time = 0
    no = 10 #no of words at a time

    for result in result.results:
        alternative = result.alternatives[0]
        #print('Transcript: {}'.format(alternative.transcript))
        #print('Confidence: {}'.format(alternative.confidence))

        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time
			
            if(len(caption.split()) == 0):
                caption = caption + word + ' '
                st_time = start_time.seconds
            elif(len(caption.split()) < no):
                caption = caption + word + ' '
                en_time = end_time.seconds # for the ending line when not a multiple of number
            else:
                caption = caption + word + ' '
                en_time = end_time.seconds
                with open('g:/sih/subtitles.srt', 'a') as f:
                    f.write(str(count) + '\n' + min(st_time) + ' --> ' + min(en_time) + '\n' + caption + '\n\n')
                caption = ''
                count += 1
            """
            print('Word: {}, start_time: {}, end_time: {}'.format(
                word,
                min(start_time.seconds),
                min(end_time.seconds)))
            """
    if(len(caption.split()) != 0):
        with open('g:/sih/subtitles.srt', 'a') as f:
            f.write(str(count) + '\n' + min(st_time) + ' --> ' + min(en_time) + '\n' + caption + '\n\n')
# [END def_transcribe_gcs]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File or GCS path for audio file to be recognized')
    args = parser.parse_args()
    transcribe_gcs_with_word_time_offsets(args.path)