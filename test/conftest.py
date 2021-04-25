import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--install-prefix",
        action="store",
        required=True,
        help="Installation prefix for the project"
    )


@pytest.fixture
def install_prefix(request):
    return request.config.getoption("--install-prefix")
