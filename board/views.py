from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import os
import glob
from snapchat import Snapchat
from shutil import copyfile
from django.shortcuts import render

PATH = './static/snappies/'
EXTENSIONS = [
    'jpeg',
    'jpg',
    'mp4',
    'webm'
]

# Create your views here.

def main(request):
  x = get_newest_snaps()
  context = { 'uno' : x[-1], 'dos' : x[-2], 'tres' : x[-3] }

  return render(request, 'index.html', context)

def get_images(request):
  s = Snapchat()
  s.login('YOUR_SNAPCHAT_USERNAME', 'YOUR_SNAPCHAT_PASSWORD')
  download_snaps(s)
  x = get_newest_snaps()
  return JsonResponse({'result' : x })

def get_newest_snaps():
  """ Get the newest snap in the thing """
  newest = glob.glob('./static/snappies/*.jpg')
  return newest

def get_downloaded():
    """ Gets the already downloaded snaps """

    result = set()

    for name in os.listdir(PATH):
        filename, ext = name.split('.')
        if ext not in EXTENSIONS:
            continue
        ts, username, id = filename.split('+')
        result.add(id)
    return result

def download(s, snap):
    """ Download a specific snap """

    id = snap['id']
    name = snap['sender']
    ts = str(snap['sent']).replace(':', '-')

    result = s.get_media(id)

    if not result:
        return False

    ext = s.is_media(result)
    filename = '{}+{}+{}.{}'.format(ts, name, id, ext)
    path = PATH + filename
    with open(path, 'wb') as fout:
        fout.write(result)
    return True

def download_snaps(s):
    """ Download snaps that haven't already been downloaded """

    existing = get_downloaded()

    snaps = s.get_snaps()
    if snaps == True or snaps == False: #sometimes the API is funky, this helps some of that
      return
    for snap in snaps:
        id = snap['id']
        if id[-1] == 's' or id in existing:
            break # if it exists, then there's no new snaps

        result = download(s, snap)

        if not result:
            print 'FAILED:', id
        else:
            print 'Downloaded:', id
            break # if you remove this line, it will download all snaps every time

