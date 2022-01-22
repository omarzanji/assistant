'''
Python 3.7 Windows 10+ install script. 
create fresh conda / venv on 3.7 for best results.
'''

import os

current_cir = os.getcwd()

os.system("pip install -r requirements.txt")
os.system("cd resources\\installer")
# os.system("pip install https://download.lfd.uci.edu/pythonlibs/x6hvwk7i/PyAudio-0.2.11-cp37-cp37m-win_amd64.whl")
os.system('resources\\installer\\Hourglassinstaller.exe')


import dload
dload.save_unzip("https://alphacephei.com/kaldi/models/vosk-model-small-en-us-0.15.zip", "modules/vosk_model")
os.rename('modules\\vosk_model\\vosk-model-small-en-us-0.15', 'modules\\vosk_model\\model')

