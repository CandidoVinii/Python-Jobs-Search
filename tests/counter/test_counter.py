from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "tests/mocks/jobs.csv"
    assert count_ocurrences(path, "full time") == 2
    assert count_ocurrences(path, "full TIME") == 2
    assert count_ocurrences(path, "end") == 3
    assert count_ocurrences(path, "intern") == 0
