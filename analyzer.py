# Za pomocą Pythona albo innego wybranego języka napisz program, który:
# Monitoruje jeden z wybranych folderów pod kątem pojawiających się plików .txt.
# Skrypt ma analizować pojawiające się pliki tekstowe (które dodajemy manualnie).
# Jeżeli plik tekstowy, który pojawił się w folderze, zawiera w środku słowo MOCAP, skrypt powinien skopiować go do innego folderu.
# Jeśli w drugim folderze pojawi się skopiowany plik, ma zostać automatycznie otwarty w notatniku.

import time
import mmap
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler


class OnWatch:
    # set the PATH to watch
    watchDirectory = Path(r"D:\Random_files_space\test_analyzer")

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
    # set the file type you want to observe for 
    def __init__(self):
        PatternMatchingEventHandler.__init__(self, patterns = ['*.txt'], ignore_directories = True, case_sensitive = False)

    # print info when defined file type created 
    def on_created(self, event):
        path = event.src_path
        print("Event occured: CREATED -", path)
        # search for MOCAP
        with open(path, 'r') as fp:
            for l_no, line in enumerate(fp):
                if 'MOCAP' in line:
                    print('MOCAP found in a file -', path)
                    print('Line number:', l_no)
                    break
        #search for MOCAP in huge files
        # with open(path,'rb',0) as file:
        #     s = mmap.mmap(file.fileno(), 0, access = mmap.ACCESS_READ)
        #     if s.find(b'MOCAP') != -1:
        #         print("MOCAP exist in a file -", path)

       
        

if __name__ == "__main__":
    watch = OnWatch()
    watch.run()

