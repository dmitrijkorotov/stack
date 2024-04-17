import pytest
from main import check_brackets

@pytest.mark.parametrize(
    "data, expected",
    (
        ['(((([{}]))))', 'Сбалансированно'],
        ['[([])((([[[]]])))]{()}',  'Сбалансированно'],
        ['{{[()]}}', 'Сбалансированно'],
        ['}{}', 'Несбалансированно'],
        ['[[{())}]', 'Несбалансированно'],
        ['{{[(])]}}', 'Несбалансированно'],
    ),
)
def test_check_brackets(data, expected):
    actual = check_brackets(data)
    assert actual == expected