import os

from django.core.management import execute_from_command_line


def test_migrateci():
    execute_from_command_line(
        [
            "manage.py",
            "migrateci",
            "--parallel",
            "2",
            "--suffix",
            "foo",
        ]
    )
    assert os.path.exists("dbtest_foo1.sqlite3")
    assert os.path.exists("dbtest_foo2.sqlite3")
    assert not os.path.exists("dbtest_foo3.sqlite3")