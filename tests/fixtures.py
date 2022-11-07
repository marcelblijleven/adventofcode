import pytest
import pytest_mock


@pytest.fixture(autouse=True)
def suppress_console(request, mocker: pytest_mock.MockerFixture):
    """
    Suppresses all console outputs by default (autouse is set to True).
    To disable for a specific test, use @pytest.mark.dontsuppress
    """
    if "dontsuppress" in request.keywords:
        return

    return mocker.patch("adventofcode.util.helpers.console")
