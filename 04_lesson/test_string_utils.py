import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()

# Тесты для capitilize
def test_capitilize_basic(utils):
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("") == ""
    assert utils.capitilize("hello world") == "Hello world"

def test_capitilize_already_uppercase(utils):
    assert utils.capitilize("Skypro") == "Skypro"

def test_capitilize_with_spaces(utils):
    assert utils.capitilize(" skypro") == " skypro"

def test_capitilize_type_error(utils):
    with pytest.raises(TypeError):
        utils.capitilize(123)
    with pytest.raises(TypeError):
        utils.capitilize(None)

# Тесты для trim
def test_trim_basic(utils):
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("  hello") == "hello"

def test_trim_no_spaces(utils):
    assert utils.trim("skypro") == "skypro"
    assert utils.trim("") == ""

def test_trim_only_spaces(utils):
    assert utils.trim("   ") == ""

def test_trim_type_error(utils):
    with pytest.raises(TypeError):
        utils.trim(123)

# Тесты для to_list
def test_to_list_basic(utils):
    assert utils.to_list("a,b,c") == ["a", "b", "c"]
    assert utils.to_list("1,2,3") == ["1", "2", "3"]

def test_to_list_custom_delimiter(utils):
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]

def test_to_list_empty(utils):
    assert utils.to_list("") == []

def test_to_list_type_error(utils):
    with pytest.raises(TypeError):
        utils.to_list(123)

# Тесты для contains
def test_contains_basic(utils):
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "U") is False

def test_contains_empty(utils):
    assert utils.contains("", "") is True
    assert utils.contains("SkyPro", "") is True

def test_contains_type_error(utils):
    with pytest.raises(TypeError):
        utils.contains(123, "a")

# Тесты для delete_symbol
def test_delete_symbol_basic(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("Hello", "l") == "Heo"

def test_delete_symbol_not_found(utils):
    assert utils.delete_symbol("SkyPro", "X") == "SkyPro"

def test_delete_symbol_empty(utils):
    assert utils.delete_symbol("", "a") == ""
    assert utils.delete_symbol("SkyPro", "") == "SkyPro"

def test_delete_symbol_type_error(utils):
    with pytest.raises(TypeError):
        utils.delete_symbol(123, "a")

# Тесты для starts_with
def test_starts_with_basic(utils):
    assert utils.starts_with("SkyPro", "S") is True
    assert utils.starts_with("SkyPro", "P") is False

def test_starts_with_empty(utils):
    assert utils.starts_with("SkyPro", "") is True
    assert utils.starts_with("", "a") is False

def test_starts_with_type_error(utils):
    with pytest.raises(TypeError):
        utils.starts_with(123, "a")

# Тесты для end_with
def test_end_with_basic(utils):
    assert utils.end_with("SkyPro", "o") is True
    assert utils.end_with("SkyPro", "y") is False

def test_end_with_empty(utils):
    assert utils.end_with("SkyPro", "") is True
    assert utils.end_with("", "a") is False

def test_end_with_type_error(utils):
    with pytest.raises(TypeError):
        utils.end_with(123, "a")

# Тесты для is_empty
def test_is_empty_basic(utils):
    assert utils.is_empty("") is True
    assert utils.is_empty(" ") is True
    assert utils.is_empty("SkyPro") is False

def test_is_empty_with_spaces(utils):
    assert utils.is_empty("  hello  ") is False

def test_is_empty_type_error(utils):
    with pytest.raises(TypeError):
        utils.is_empty(123)

# Тесты для list_to_string
def test_list_to_string_basic(utils):
    assert utils.list_to_string([1, 2, 3]) == "1, 2, 3"
    assert utils.list_to_string(["a", "b", "c"]) == "a, b, c"


def test_list_to_string_custom_joiner(utils):
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"

def test_list_to_string_empty(utils):
    assert utils.list_to_string([]) == ""

def test_list_to_string_type_error(utils):
    with pytest.raises(TypeError):
        utils.list_to_string("not a list")
    with pytest.raises(TypeError):
        utils.list_to_string([1, 2], 123)
