# Za pomocą Pythona albo innego wybranego języka napisz program, który:
# Monitoruje jeden z wybranych folderów pod kątem pojawiających się plików .txt.
# Skrypt ma analizować pojawiające się pliki tekstowe (które dodajemy manualnie).
# Jeżeli plik tekstowy, który pojawił się w folderze, zawiera w środku słowo MOCAP, skrypt powinien skopiować go do innego folderu.
# Jeśli w drugim folderze pojawi się skopiowany plik, ma zostać automatycznie otwarty w notatniku.

import os
import time
import shutil
import subprocess as sp
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from prefect import task

input_folder = Path(r"D:\Random_files_space\test_analyzer\input")
output_folder = Path(r"D:\Random_files_space\test_analyzer\output")
notepad_path = Path(r"C:\Windows\notepad.exe")

class OnWatch():
    ## Set the PATH to watch
    watchDirectory = input_folder

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = MyHandler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer stopped!")

        self.observer.join()

class MyHandler(PatternMatchingEventHandler):
    ## Set the file type you want to observe for 
    def __init__(self):
        PatternMatchingEventHandler.__init__(self, patterns = ['*.txt'], ignore_directories = True, case_sensitive = False)

    ## Print info when defined file type created 
    def on_created(self, event):
        path = event.src_path
        txt_file = Path(path).name
        print(f"Processing:", txt_file)
        
        print("Event occured: CREATED -", path)

        ## Search for MOCAP
        with open(path, 'r') as fp:
            for l_no, line in enumerate(fp):
                if 'MOCAP' in line:
                    print('MOCAP found in a file -', path)
                    # print('Line number:', l_no)

        ## Search for MOCAP in huge files
        # with open(path,'rb',0) as file:
        #     s = mmap.mmap(file.fileno(), 0, access = mmap.ACCESS_READ)
        #     if s.find(b'MOCAP') != -1:
        #         print("MOCAP exist in a file -", path)

                    ## Coppy a file to output directory 
                    shutil.copy(path, output_folder)
                    print ('Event occured: COPPIED TO -', output_folder)
                    time.sleep(3)

                    ## Open coppied file in notepad
                    file_path = os.path.join(output_folder, txt_file + ".")
                    sp.call([notepad_path, file_path])
                    break     

if __name__ == "__main__":
    watch = OnWatch()
    watch.run()
