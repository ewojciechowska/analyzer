# Za pomocą Pythona albo innego wybranego języka napisz program, który:
# Monitoruje jeden z wybranych folderów pod kątem pojawiających się plików .txt.
# Skrypt ma analizować pojawiające się pliki tekstowe (które dodajemy manualnie).
# Jeżeli plik tekstowy, który pojawił się w folderze, zawiera w środku słowo MOCAP, skrypt powinien skopiować go do innego folderu.
# Jeśli w drugim folderze pojawi się skopiowany plik, ma zostać automatycznie otwarty w notatniku.

import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler

class OnWatch:
    # set the directory to watch
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
    def __init__(self):
        PatternMatchingEventHandler.__init__(self, patterns = ['*.txt'], ignore_directories = True, case_sensitive = False)

    def on_created(self, event):
        print("Event occured: CREATED - % s." % event.src_path)


if __name__ == "__main__":
    watch = OnWatch()
    watch.run()
