import unittest

from bs4 import BeautifulSoup

from grim_calc.utils.html_utils import remove_non_tags, get_child_tag_containing_class, get_child_tag_containing_string

SIMPLE_HTML = """<div>Hello</div>"""


class UnitTest(unittest.TestCase):
    @staticmethod
    def test_remove_non_tags():
        example_tag = BeautifulSoup(SIMPLE_HTML, "html.parser")
        input_list = [
            "",
            example_tag,
            "",
            example_tag,
        ]
        expected_list = [example_tag, example_tag]
        actual_list = remove_non_tags(input_list)
        assert expected_list == actual_list

    @staticmethod
    def test_get_child_tag_containing_class():
        class_name = "target-class"
        expected_tag = BeautifulSoup(
            f'<div class="{class_name} other-class">contents</div>', "html.parser"
        ).div
        tag_to_skip = BeautifulSoup(
            '<div class="item-type">One-Handed Sword</div>', "html.parser"
        ).div
        input_tags = [expected_tag, tag_to_skip]
        actual_tag = get_child_tag_containing_class(input_tags, class_name)
        assert expected_tag == actual_tag

    @staticmethod
    def test_get_child_tag_containing_string():

        contents = "target_contents"
        expected_tag = BeautifulSoup(f"<div>{contents}</div>", "html.parser")
        tag_to_skip = BeautifulSoup("<div>contents</div>", "html.parser")
        input_tags = [expected_tag, tag_to_skip]
        actual_tag = get_child_tag_containing_string(input_tags, contents)
        assert expected_tag == actual_tag


if __name__ == "__main__":
    unittest.main()
