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
    result = {}
    with open(path, "r") as input_file:
        for (line) in input_file:  # reading a file line by line without loading it into memory
            if not line.startswith("#"):
                if line == "\n":
                    if result:
                        yield result
                        result = {}
                        continue
                    else:
                        continue
                match = re.search(r"^\w*-*\w*(?=:)", line)
                if match:
                    key, value = re.split(r":\s*(?=[\w*])", line)
                    if key in result.keys():
                        result[key] += value  # for duplicate keys
                    else:
                        result[key] = value
                else:
                    last_key = list(result)[-1]
                    line = line.replace("                ", "")  # for multiline records
                    result[last_key] += line


def load_data(path: str) -> None:
    parsed_data = parse_file(path)

    for document in parsed_data:
        print(document)  # load document to database (or do something else)


if __name__ == "__main__":
    load_data("some_text.txt")
