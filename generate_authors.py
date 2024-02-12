#!/usr/bin/python3
"""Generate Authors file"""


AUTHORS_CONTENT = """
This is the list of contributors to the project:

- Adeshina Ibrahim <Adeshinaibrahim10@gmail.com>
- Favour Nwaneri <>
"""

def generate_authors_file():
    """ Generates authors file"""
    with open("AUTHORS", "w") as f:
        f.write(AUTHORS_CONTENT)

if __name__ == "__main__":
    generate_authors_file()
