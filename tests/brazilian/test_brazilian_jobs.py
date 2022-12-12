from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    for translate in read_brazilian_file(path):
        assert 'titulo' not in translate
        assert 'salario' not in translate
        assert 'tipo' not in translate
        assert 'type' in translate
        assert 'salary' in translate