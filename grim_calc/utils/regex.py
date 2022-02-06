import re

REGEX_1_TO_999 = "[0-9]{1,3}"
REGEX_1_TO_99 = "[0-9]{1,2}"
REGEX_1_TO_9 = "[0-9]"

NUMBER_SINGLE = f"({REGEX_1_TO_999})"
NUMBER_RANGE = f"({REGEX_1_TO_999})/({REGEX_1_TO_999})"
NUMBER_RANGED = (
    f"({REGEX_1_TO_999})-({REGEX_1_TO_999})/({REGEX_1_TO_999})-({REGEX_1_TO_999})"
)
CAMEL_CASE_REGEX = re.compile(r"[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))")


def camel_case_to_sentence(camel: str) -> str:
    return " ".join(CAMEL_CASE_REGEX.findall(camel))
