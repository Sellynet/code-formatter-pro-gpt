from code_formatter_pro.core import format_code

def test_format_code():
    ugly = "def f():\n print('hi')"
    pretty = format_code(ugly)
    assert "def f():" in pretty and "    print(\"hi\")" in pretty
