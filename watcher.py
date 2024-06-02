import subprocess
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class Watcher:
    DIRECTORY_TO_WATCH = "."

    def __init__(self, script):
        self.observer = Observer()
        self.script = script

    def run(self):
        event_handler = Handler(self.script)
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script

    def on_modified(self, event):
        if event.src_path.endswith(self.script):
            print(f"{self.script} has been modified. Re-running...")
            subprocess.run([sys.executable, self.script])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python watcher.py <script_to_watch>")
        sys.exit(1)
    script_to_watch = sys.argv[1]
    watcher = Watcher(script_to_watch)
    watcher.run()
