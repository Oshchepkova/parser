import re
from typing import Dict


def parse_file(path: str) -> Dict[str, str]:
    """file parsing function in format:
    key1:       value1
    key2:       value2
    key3:       value3

    key4:       value4
    key5:       value5
    key6:       value6
    """

    with open(path, "r") as input_file:
        data = input_file.read()
    chunk_data = data.split("\n\n")
    for document in chunk_data:
        result = {}
        blocs = document.split("\n")
        for record in blocs:
            if not record.startswith("#"):
                match = re.search(r"^\w*-*\w*(?=:)", record)
                if match:
                    key, value = re.split(r":\s*(?=[\w*])", record)
                    if key in result.keys():
                        result[key] += "\n " + value  # for duplicate keys
                    else:
                        result[key] = value
                else:
                    last_key = list(result)[-1]
                    record = record.replace(
                        "                ", "\n"
                    )  # for multiline records
                    result[last_key] += record
        if result:
            yield result


def load_data(path: str) -> None:
    parsed_data = parse_file(path)

    for document in parsed_data:
        print(document)  # load document to database (or do something else)


if __name__ == "__main__":
    load_data("some_text.txt")
