"""
Language listing generation.
"""

from glob import glob
import os
import yaml


def get_table_rows():
    "Get markdown table for docs."
    thisdir = os.path.dirname(__file__)
    langglob = os.path.join(thisdir, "**", "definition.yaml")
    output = []
    for filename in glob(langglob):
        with open(filename, "r", encoding="utf-8") as f:
            y = yaml.safe_load(f)
            langname = y["name"]
            if langname != "Generic":
                output.append(f"* {langname}")
    output.sort()
    return output


def generate_list():
    "Gen list"
    rows = get_table_rows()
    print("\n".join(rows))


if __name__ == "__main__":
    generate_list()
