import os
import sys
from tqdm import tqdm
from urllib.parse import urlparse
from urllib.request import urlretrieve
from zipfile import ZipFile

linux_executables = ["steam.sh", "steam_msg.sh", "ubuntu12_32/fossilize_replay", "ubuntu12_32/gameoverlayui", "ubuntu12_32/gldriverquery", "ubuntu12_32/reaper", "ubuntu12_32/steam", "ubuntu12_32/steam-launch-wrapper", "ubuntu12_32/steam_monitor", "ubuntu12_32/steamui.so", "ubuntu12_32/streaming_client", "ubuntu12_32/vulkandriverquery", "ubuntu12_64/disk-free", "ubuntu12_64/fossilize_replay", "ubuntu12_64/gldriverquery", "ubuntu12_64/steam-runtime-heavy.sh", "ubuntu12_64/steamwebhelper", "ubuntu12_64/steamwebhelper.sh", "ubuntu12_64/streaming_client", "ubuntu12_64/vulkandriverquery"]

class ProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download(url, file_name):
    with ProgressBar(unit='B', unit_scale=True, miniters=1, desc=file_name) as t:
        urlretrieve(url, filename=file_name, reporthook=t.update_to)

def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2
    os.chmod(path, mode)

def main():
    if len(sys.argv) != 2:
        print("Need links file argument")
        sys.exit(1)

    with open(sys.argv[1], "r") as links_file:
        os.mkdir("Steam")
        os.chdir("Steam")

        for asset in links_file:
            parsed = urlparse(asset)
            bsn = os.path.basename(parsed.path)
            name = bsn[:bsn.rfind(".")]

            download(asset, name)

            if sys.platform != "win32":
                os.path.altsep = "\\"

            with ZipFile(name, "r") as asset_zip:
                asset_zip.extractall()

            os.remove(name)

    if sys.platform == "linux":
        for executable in linux_executables:
            make_executable(executable)
