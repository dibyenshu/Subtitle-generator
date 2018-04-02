#uploads file to the server with public readability
from subprocess import call

#call(cmd,shell=True)
call('cd g:/sih && gsutil cp audio.flac gs://sih2018',shell=True)

#not required anymore after making sih 2018 bucket public
#call('gsutil acl ch -u AllUsers:R gs://sih2018/audio.flac',shell=True)
