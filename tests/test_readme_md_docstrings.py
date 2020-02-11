import os
import shutil
from urllib.parse import urljoin

from readme_md_docstrings import ReadMe, update

DATA_DIRECTORY: str = urljoin(
    __file__,
    './data/'
)


def test_update() -> None:
    template_path: str = urljoin(__file__, './TEMPLATE.md')
    readme_path: str = urljoin(__file__, './README.md')
    shutil.copy(
        template_path,
        readme_path
    )
    current_directory: str = urljoin(__file__, './')
    os.chdir(current_directory)
    update()


if __name__ == '__main__':
    test_update()

