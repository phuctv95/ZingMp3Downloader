Instruction using on Linux:

  1. To make `zingmp3_downloader.sh` running everywhere, run following code:
    ```sh
    $ sudo ln -s path/to/zingmp3_downloader.sh /usr/local/bin/zingmp3_downloader`
    ```

  2. Now to download any song, type following command:
    ```sh
    $ zingmp3_downloader url_song [quality]`
    ```
    - `url_song` is the url to the ZingMp3 song, e.g. http://mp3.zing.vn/bai-hat/Oh-NaNa-KARD/ZW78BOO7.html
    - `quality` is either 128 or 320 (kbps). Leave it blank will download in 128kbps.
  
  Downloaded file will save to ~/Downloads/
