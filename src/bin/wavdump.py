import urllib
from urllib.parse import urlparse
import sys

url = sys.argv[1]
req = urllib.Request(url)
handler = urllib.urlopen(req)
buffer = handler.read()
sys.stdout.write(buffer)
sys.stdout.flush()

