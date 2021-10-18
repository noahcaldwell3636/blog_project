""" This script can be run from the devlopment 
environment to output the URL structure of this 
django project.

(BROKEN!)
"""

import subprocess
from pprint import pprint


def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

if __name__ == '__main__':
    print("start")
    django_urls = run("python manage.py show_urls")
    url_list = str(django_urls).split(r"\n") 
    result = []
    index = 0
    for url in url_list:
        url.replace("/", "", 1)
        sectioned_url = url.split("/")
        index = 0
        for section in sectioned_url:
            if section in result