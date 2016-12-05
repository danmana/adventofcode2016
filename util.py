import os
import browser_cookie3
import requests


def maybe_download(day):
    temp_dir = 'temp'
    if not os.path.isdir(temp_dir):
        os.makedirs(temp_dir)
    day_dir = os.path.join(temp_dir, 'day_%02d' % day)
    if not os.path.isdir(day_dir):
        os.makedirs(day_dir)
    file_name = os.path.join(day_dir, 'in.txt')
    if not os.path.exists(file_name):
        url = 'http://adventofcode.com/2016/day/%d/input' % day
        cookies = browser_cookie3.firefox(domain_name='adventofcode.com')
        response = requests.get(url, cookies=cookies)
        with open(file_name, 'wb') as file:
            file.write(response.content)
    return open(file_name, 'r')
