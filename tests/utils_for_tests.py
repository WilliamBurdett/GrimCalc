import os

from bs4 import Tag, BeautifulSoup


def open_item_file(file_name: str) -> Tag:
    path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(path, "item_html_examples", f"{file_name}.html"), "r") as f:
        contents = f.read()
    example_tag = BeautifulSoup(contents, "html.parser")
    return example_tag
