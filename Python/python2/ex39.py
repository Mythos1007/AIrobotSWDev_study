from urllib import request
from urllib import parse, error, robotparser, response
from math import sin, cos, tan

target = urllib.request.urlopen('http://google.com').read()
print(target)

