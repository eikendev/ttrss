from ttrss.util import *


def test_get_valid_filename():
    assert get_valid_filename("FOO  BAR") == "foo_bar"
