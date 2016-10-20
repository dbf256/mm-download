# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
import sys
import os

if len(sys.argv) < 2:
    print u'Usage: python mm_download.py pattern [output_directory]'
    sys.exit(1)

pattern = sys.argv[1]

if len(sys.argv) > 2:
    output_dir = sys.argv[2]
else:
    output_dir = None

BASE_URL = u'http://direct.mapswithme.com/regular/daily/'

index_page = urllib2.urlopen(BASE_URL).read()

files = re.findall(r'href=[\'"]?([^\'" >]+)', index_page)
files = map(lambda u: unicode(u), files)
files = filter(lambda u: u'mwm' in u, files)
files = filter(lambda u: pattern.lower() in u.lower(), files)

print u'File(s) to process: ' + u', '.join(files)

if output_dir is not None:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

for f in files:
    url = BASE_URL + f
    filename = f.replace(u'%20', u' ')
    if output_dir is not None:
        filename = os.path.join(output_dir, filename)
    print u'Downloading: ' + f + u' to ' + filename
    urllib.urlretrieve(url, filename)

print u'Downloaded ' + unicode(len(files)) + u' file(s)'
