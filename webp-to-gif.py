#!/usr/bin/env python

import sys
import requests


def main():
    if len(sys.argv) == 3:
        download_and_save(sys.argv[1], sys.argv[2])
    else:
        sys.exit("Usage: python3 webp_to_gif.py <URL>")


def download_and_save(URL, name):
    response = requests.get(URL)
    with open(f"{name}.gif", "wb") as fd:
        for chunk in response.iter_content(chunk_size=128):
            fd.write(chunk)


if __name__ == "__main__":
    main()
