# ZingMp3 Downloader
Instruction using on Linux:
  1. Make sure you installed Python.

  2. Run `installer.sh` will make program running everywhere (installer will link program to `/usr/local/bin`, so you need to type the password for the linking).
  
  3. Now to download any song, type following command:
    ```sh
    $ zingmp3_downloader song_url [quality]
    ```
    - `song_url` is the url to the ZingMp3 song, e.g. http://mp3.zing.vn/bai-hat/Oh-NaNa-KARD/ZW78BOO7.html
    - `quality` is either 128 or 320 (kbps). Leave it blank will download in 128kbps.
  
  Downloaded file will save to ~/Downloads/
