import io
import sys
import importlib
from typing import Generator


def list_module_contents(module_name: str) -> Generator[str, None, None]:
    module = importlib.import_module(module_name)

    with io.StringIO() as buffer:
        for attr in dir(module):
            print(attr, file=buffer)

        top_items = buffer.getvalue()
        for item in top_items.split('\n'):
            yield item
