# Za pomocą Pythona albo innego wybranego języka napisz program, który:
# Monitoruje jeden z wybranych folderów pod kątem pojawiających się plików .txt.
# Skrypt ma analizować pojawiające się pliki tekstowe (które dodajemy manualnie).
# Jeżeli plik tekstowy, który pojawił się w folderze, zawiera w środku słowo MOCAP, skrypt powinien skopiować go do innego folderu.
# Jeśli w drugim folderze pojawi się skopiowany plik, ma zostać automatycznie otwarty w notatniku.

import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("File {event.src_path} has been created")

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path= Path(r"D:\Random_files_space\test_analyzer"), recursive=True)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
