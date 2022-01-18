import subprocess


def start():
    """
    Run all unittests.
    Will be used by poetry to run all test.
    Equivalent to: `poetry run python -u -m pytest tests --cov=./src`
    Will generate coverage report as well.
    """
    subprocess.run(["python", "-u", "-m", "pytest", "tests", "--cov=./src"])
