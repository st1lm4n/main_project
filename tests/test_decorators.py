from src.decorators import log


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(4, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_():
    @log()
    def my_func(x, y):
        return x / y

    assert my_func(4, 2) == 2
    assert my_func("4", 2) is None
    assert my_func(4, 0) is None
    assert my_func(0, 4) == 0


def test_log_file():
    @log(filename="tests/logs/log.txt")
    def my_func(x, y):
        return x / y

    assert my_func(4, 2) == 2
    assert my_func("4", 2) is None
    assert my_func(4, 0) is None
    assert my_func(0, 4) == 0


@log()
def my_function(x, y):
    return x + y


def test_log_console_ok(capsys):
    my_function(2, 3)
    output = capsys.readouterr()
    assert output.out == "my_function ok\n"


def test_log_console_arror(capsys):
    my_function(2, "3")
    output = capsys.readouterr()
    assert output.out == "my_function error: TypeError. Inputs: (2, '3'), {}\n"
