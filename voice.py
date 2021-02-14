import pyttsx3
import subprocess
#import ftransc
import ffmpeg


""" HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0 []
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0 []
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0 []
 """
engine = pyttsx3.init()
engine.setProperty(
    "voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0")
# engine.say("Работает")


def text_to_speech(text):
    fn = "data/test.mp3"
    #fout = "data/test.ogg"
    engine.save_to_file(text, fn)
    engine.runAndWait()
    # ffmpeg -i input.mp3 -c:a libopus output.opus
    #subprocess.run = (["ffmpeg", "-i", fn, "-c:a", "libopus", fout])
    # ftransc -f ogg fn
    return fn
