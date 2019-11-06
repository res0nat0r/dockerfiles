#!/usr/bin/env python

from googlesearch import search 
import sys

for res in search("imdb " + sys.argv[1], tld="com", num=1, stop=1, pause=2):
  print(res)