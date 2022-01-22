import re
from typing import Union, List

from bs4 import Tag, NavigableString

NON_DECIMAL = re.compile(r"[^\d.]+")

def get_item_type(div: Tag) -> str:
    inner_contents = remove_non_tags(div.div.contents)
    item_description = remove_non_tags(inner_contents[1].contents)
    item_type = item_description[1].contents[0]
    return item_type


def strip_non_numeric(tag: Union[Tag, str]) -> Union[float, int]:
    numeric_only = NON_DECIMAL.sub("", str(tag))
    if "." in numeric_only:
        return float(numeric_only)
    return int(numeric_only)


def remove_non_tags(all_children: List[Union[Tag, NavigableString]]) -> List[Tag]:
    children = []
    for child in all_children:
        if isinstance(child, Tag):
            children.append(child)
    return children


def get_child_tag_containing_class(contents: List[Tag], class_name: str) -> Tag:
    for tag in contents:
        if "class" in tag.attrs.keys():
            if class_name in tag["class"]:
                return tag


def get_child_tag_containing_string(contents: List[Tag], string: str) -> Tag:
    for tag in contents:
        if string in str(tag):
            return tag

