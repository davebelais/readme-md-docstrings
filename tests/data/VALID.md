# readme-md-docstrings

Modi dolore labore porro porro dolor. Numquam consectetur adipisci dolore 
consectetur porro dolore. Aliquam amet consectetur porro neque. Porro ipsum
velit quaerat ipsum etincidunt amet neque. Adipisci quisquam eius velit numquam 
eius sed dolor. Adipisci dolorem tempora consectetur non quiquia sed. Quisquam
tempora aliquam quaerat. Est quiquia ipsum quiquia dolor est. Sed dolore ut
quiquia. Amet quisquam porro est.

## Test code-block comments

```shell script
pip3 install readme-md-docstrings

# Comment 1
a: int = 0

## Comment 2
b: int = 1

### Comment 3
b: int = 2
```

## Test module and class documentation

### readme_md_docstrings

This module may be called as a command-line executable. For example:
```shell script
python3 -m readme_md_docstrings ./README.md
```

If no path is provided, the default is "./README.md":
```shell script
python3 -m readme_md_docstrings
```

#### ReadMe

This class parses a markdown-formatted README file and updates sections
to reflect a corresponding package's class, method, and function
docstrings.

Parameters:

- markdown (str): Markdown-formatted text

```python
from readme_md_docstrings import ReadMe
# Read the existing markdown
path: str = './README.md'
with open(path, 'r') as readme_io:
    read_me: ReadMe = ReadMe(readme_io.read())
read_me_str: str = str(read_me).rstrip()
# Update and save
if read_me_str:
    with open(path, 'w') as readme_io:
        readme_io.write(read_me_str)
```

#### update

Update an existing markdown-formatted README file based on any headers
matching (fully-qualified) module, class, or function docstrings.

```python
import readme_md_docstrings
readme_md_docstrings.update('./README.md')
```

#### Unmatched
