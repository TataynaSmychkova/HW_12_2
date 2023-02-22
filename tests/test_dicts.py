from utils.dicts import get_val


def test_dicts():
    assert get_val([], "key") == 'Не верные данные'
    assert get_val({"test": 2}, "key") == 'git'
    assert get_val({"test": 2}, "test") == 2



