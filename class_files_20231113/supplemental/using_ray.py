# pip install ray[default]
import time
import ray
import requests
from bs4 import BeautifulSoup

@ray.remote
def get_data(url: str):
    try:
        text = requests.get(url).text
        soup = BeautifulSoup(text, 'html.parser')
        result = soup.title.text
    except (TypeError, requests.exceptions.ConnectionError) as err:
        result = err.args[0]

    return result


tasks = ['https://requests.readthedocs.io/en/latest/', 'https://upjoke.com/python-jokes', 'https://pypi.python.org',
         'https://pandas.pydata.org/pandas-docs/stable/', 'http://www.python.org',
         'http://love-python.blogspot.com/', 'http://planetpython.org', 'https://www.python.org/doc/humor/',
         'https://doughellmann.com/blog/', 'https://pymotw.com/3/', 'http://python-history.blogspot.com/',
         'https://nothingbutsnark.svbtle.com/','https://www.pydanny.com/','https://pythontips.com/',
         'http://www.blog.pythonlibrary.org/', 'https://minhhh.github.io/posts/a-guide-to-pythons-magic-methods']

print('Starting...')
obj_refs = [get_data.remote(url) for url in tasks]
results = ray.get(obj_refs)
print(*results, sep='\n')
ray.timeline(filename='timeline.json')

# open chrome to...chrome://tracing/
# "Load" the timeline.json file.