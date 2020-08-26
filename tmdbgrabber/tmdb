#!/usr/bin/env python

from io import BytesIO
import fnmatch
import os
import re
import requests
from PIL import Image


KEY = $KEY_HERE


def get_configuration():
    url = "https://api.themoviedb.org/3/configuration?api_key={}".format(KEY)

    r = requests.get(url)
    return r.json()['images']['base_url']


def find_nfos():
    nfos = []

    for root, _, files in os.walk('.'):
        for nfo in files:
            if fnmatch.fnmatch(nfo, '*.nfo'):
                nfos.append(root + "/" + nfo)

    return nfos


def grab_imdb_url(nfo):
    for line in open(nfo):
        if re.findall(r'imdb.com.title.(tt\d+)', line):
            return re.findall(r'imdb.com.title.(tt\d+)', line)[0]


def lookup_tmdb_id(imdb_id):
    url = "https://api.themoviedb.org/3/find/{}?api_key={}" \
          "&language=en-US&external_source=imdb_id".format(imdb_id, KEY)

    r = requests.get(url)
    return r.json()['movie_results'][0]['id']


def download_images(tmdb_id, movie_dir):
    url = "https://api.themoviedb.org/3/movie/{}/images?api_key={}" \
          "&language=en-US&include_image_language=en,null".format(tmdb_id, KEY)

    collection = requests.get(url).json()

    for backdrop in collection['backdrops']:
        backdrop_url = "{}original{}".format(base_url, backdrop['file_path'])
        image_path = os.path.dirname(movie_dir) + "/backdrop-" + os.path.basename(backdrop_url)

        if not os.path.exists(image_path):
            image = Image.open(BytesIO(requests.get(backdrop_url).content))
            image.save(image_path)

    for poster in collection['posters']:
        poster_url = "{}original{}".format(base_url, poster['file_path'])
        poster_path = os.path.dirname(movie_dir) + "/poster-" + os.path.basename(poster_url)

        if not os.path.exists(poster_path):
            poster = Image.open(BytesIO(requests.get(poster_url).content))
            poster.save(poster_path)


base_url = get_configuration()
[download_images(lookup_tmdb_id(grab_imdb_url(nfo)), nfo) for nfo in find_nfos()]
