
import os

import speaker
from shell_cmd import run_shell_cmd

def main():
    curdir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
    
    tflite_path = f'{curdir}/keyword_spotting_on_off.tflite'
    exe_path = f'{curdir}/audio_classifier.exe'

    def _line_callback(line):
        print(line.strip())
        if 'Heard on' in line:
            speaker.unmute()
        elif 'Heard off' in line:
            speaker.mute()

    run_shell_cmd(
        [exe_path, '-m', tflite_path, '--threshold', 150, '--latency', 150, '--volume', 0],
        line_processor=_line_callback
    )


if __name__ == '__main__':
    main()