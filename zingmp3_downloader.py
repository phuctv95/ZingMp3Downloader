import urllib2,cookielib
import json
import sys
import os

# DEFINE SOMETHING --------------------------------------------------------------------------------

'''
Function that returns the source from the target url
@param url  
'''
def file_get_contents(url):
    url = str(url).replace(" ", "+") # just in case, no space in url
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    req = urllib2.Request(url, headers=hdr)
    try:
        page = urllib2.urlopen(req)
        return page.read()
    except urllib2.HTTPError, e:
        print e.fp.read()
    return ''

# Data here
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
input_link = "" # example: "http://mp3.zing.vn/bai-hat/Blood-Sweat-Tears-BTS/ZW78O7EE.html"
download_quality = "" # 128 or 320
output_dir = os.path.expanduser('~') + "/Downloads" # is the ~/Downloads path
output_filename = ""
song_id = ""
api_zingmp3_link_format = "http://api.mp3.zing.vn/api/mobile/song/getsonginfo?requestdata={{\"id\":\"{}\"}}"
api_zingmp3_link = ""
json_content = ""
download_link = ""
song_title = ""
song_article = ""


# PROGRAM STARTING POINT --------------------------------------------------------------------------

# Get arguments >> input_link, download_quality
number_args = len(sys.argv)
if number_args != 2 and number_args != 3 :
    print "Invalid arguments! Numbers of argument must be 1 or 2."
    print "- First argument is the ZingMp3 link"
    print "- [Optional] Second argument is the download quality: 128 or 320"
    print 
    exit()
input_link = sys.argv[1]
if len(sys.argv) == 2 :
    download_quality = "128"
else:
    download_quality = sys.argv[2]
print "Link music: \t\t" + input_link
print "Download quality: \t" + download_quality + "kbps"
print ""

# Get id, api link >> song_id, api_zingmp3_link
song_id = input_link.split("/")[-1].split(".")[0]
api_zingmp3_link = api_zingmp3_link_format.format(song_id)
print "Song id: \t\t" + song_id
print "API link: \t\t" + api_zingmp3_link
print ""

# Get JSON content >> json_content
json_content = json.loads(file_get_contents(api_zingmp3_link))
song_title = json_content["title"]
song_article = json_content["artist"]
print "Song info - Artist(s): \t" + song_article
print "Song info - Title: \t" + song_title
print ""

# Get link download >> download_link
if download_quality == "128" :
    download_link = json_content["link_download"]["128"]
    print "Download link: \t\t" + download_link
    print ""
elif download_quality == "320" :
    download_link = json_content["link_download"]["320"]
    print "Download link: \t\t" + download_link
    print ""

# Download song save to current directory
file_name = song_article + " - " + song_title + ".mp3"
print "File will saved as: \t{}".format(output_dir + "/" + file_name)
sys.stdout.write("Download status: \tDownloading...")
sys.stdout.flush()
request = urllib2.Request(download_link, headers=hdr)
try:
    content = urllib2.urlopen(request)
    with open(output_dir + "/" + file_name, "wb") as local_file:
        local_file.write(content.read())
    sys.stdout.write("\b\b\b\b\b\b\b\b\b\b\b\b\b\bFinished!     ")
    sys.stdout.flush()
    print ""
    print ""
except urllib2.HTTPError, e:
    sys.stdout.write("\b\b\b\b\b\b\b\b\b\b\b\b\b\bDownload failed :(")
    sys.stdout.flush()
    print ""
    print "\t\t\tHTTP Error Code: {}".format(e.code)