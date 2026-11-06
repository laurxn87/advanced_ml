import subprocess 
from pathlib import Path 

class LibrespotManager: 

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.cache_dir = Path(project_root, "cache", "librespot")
        self.process = None

    def start(self):
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        command = command = [
            "librespot",
            "--name", "controlla",
            "--bitrate", "320",
            "--cache", str(self.cache_dir),
        ]

        self.process = subprocess.Popen(command)


    def stop(self):
        if self.process is not None:
            self.process.terminate()
            self.process.wait()
            self.process = None