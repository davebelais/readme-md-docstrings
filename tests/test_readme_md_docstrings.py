"""
Note: If/when docstrings are updated anywhere in the package--it will be
necessary to delete the validation file (./data/VALID.md), re-run
`test_update()`, then manually verify the output.
"""
import shutil
import sys
from subprocess import getstatusoutput
from urllib.parse import urljoin
from warnings import warn

from readme_md_docstrings import update

TEMPLATE_PATH: str = urljoin(__file__, './data/TEMPLATE.md')
TEST_PATH: str = urljoin(__file__, './data/TEST.md')
VALID_PATH: str = urljoin(__file__, './data/VALID.md')


def _get_valid() -> str:
    """
    Obtain a string containing the text which *should* be found in
    ./data/TEST.md after an update.
    """
    valid_text: str = ''
    try:
        with open(VALID_PATH, 'r') as valid_io:
            valid_text: str = valid_io.read()
    except FileNotFoundError:
        # If no validated output has been saved previously—-create it now
        shutil.copy(
            TEST_PATH,
            VALID_PATH
        )
    return valid_text


def _validate_test() -> None:
    """
    Verify that the content of ./data/TEST.md matches our expected output
    """
    valid_text: str = _get_valid()
    if valid_text:
        # If the validation file was pre-existing, compare it with the output we
        # just wrote
        with open(TEST_PATH, 'r') as test_io:
            assert test_io.read() == valid_text
    else:
        # If the validation file was not pre-existing, the user should manually
        # validate the newly created file to ensure it matches expectations
        warn(
            '*./data/VALIDATE.md* was not pre-existing, please manually verify '
            'the newly generated contents of this file'
        )


def _command_line_update(path: str) -> None:
    """
    Use this package as a CLI, passing `path` as the only argument, and raise
    any errors returned
    """
    status: int
    output: str
    status, output = getstatusoutput(
        f'{sys.executable} -m readme_md_docstrings {path}'
    )
    if status:
        raise OSError(output)


def test_update(
    _iteration: int = 0,
    command_line_interface: bool = False,
    *args  # This prevents accidentally passing a positional argument
) -> None:
    """
    Update a template README file from this module and compare it against the
    expected output.

    Note: If/when docstrings are updated anywhere in this package--it will be
    necessary to delete the validation file (./data/VALID.md), then re-run this
    unit test and manually verify the output.

    Parameters:

    (no *public* parameters)
    """
    # Ensure that the parameters received are valid
    if args:
        raise ValueError(
            'No parameters should be passed to this function'
        )
    assert isinstance(_iteration, int)
    # If this is not a recursive call, start with a copy of the template file
    if not _iteration:
        shutil.copy(
            TEMPLATE_PATH,
            TEST_PATH
        )
    # Update the test file from our docstrings
    if command_line_interface:
        _command_line_update(TEST_PATH)
    else:
        update(TEST_PATH)
    # Perform one recursive call, to ensure that nothing odd occurs when
    # *existing* text is found for a heading or sub-heading
    if not _iteration:
        test_update(_iteration + 1)


def test_command_line_update() -> None:
    """
    This test is identical to `test_update`, excepting that it executes
    tests through the command line.
    """
    test_update(command_line_interface=True)


if __name__ == '__main__':
    test_update()
    test_command_line_update()

