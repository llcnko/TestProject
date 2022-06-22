import pytest


@pytest.mark.usefixtures("init_chrome")
class ParentTest:
    pass
