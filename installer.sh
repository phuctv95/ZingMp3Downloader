#!/bin/bash

current_path=$(pwd)
echo "python $current_path/zingmp3_downloader.py \$1 \$2" > zingmp3_downloader
chmod +x zingmp3_downloader
sudo ln -s "$current_path/zingmp3_downloader" "/usr/local/bin/zingmp3_downloader"
