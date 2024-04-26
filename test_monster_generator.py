from pytest import approx
from monster_generator import read_cr_table, find_cr_level
from tempfile import mktemp
import pytest

def test_read_cr_table():
    assert 0 == 0
    cr_dict = read_cr_table("cr_table.csv")

    assert cr_dict['0'][0] == '2'
    assert cr_dict["0"] == ['2', '13', ['1', '6'], '3', ['0', '1'], '13']
    assert cr_dict["30"] == ['9', '19', ['806', '850'], '14', ['303', '320'], '23']

    assert type(cr_dict["1_4"][2]) is list
    assert type(cr_dict["1_4"][4]) is list
    assert type(cr_dict["1"][2]) is list
    assert type(cr_dict["1"][4]) is list
    assert type(cr_dict["9"][2]) is list
    assert type(cr_dict["9"][4]) is list

    assert type(cr_dict["1_4"][1]) is str
    assert type(cr_dict["1_4"][3]) is str
    assert type(cr_dict["1"][1]) is str
    assert type(cr_dict["1"][3]) is str
    assert type(cr_dict["9"][1]) is str
    assert type(cr_dict["9"][3]) is str

    #Be sure it raises appropriate errors
    filename = mktemp(dir=".", prefix="not", suffix=".csv")
    with pytest.raises(FileNotFoundError):
        read_cr_table(filename)
        pytest.fail("read_dictionary function must use its filename parameter")


def test_find_cr_level():
    cr_dict = read_cr_table("cr_table.csv")
    HP_INDEX = 2
    ARMOR_CLASS_INDEX = 1

    assert find_cr_level(cr_dict, HP_INDEX, 50)[0] == "1_2"
    assert find_cr_level(cr_dict, HP_INDEX, 2)[0] == "0"
    assert find_cr_level(cr_dict, HP_INDEX, 223)[0] == "11"
    assert find_cr_level(cr_dict, ARMOR_CLASS_INDEX, 13) == ("3", "0")
    assert find_cr_level(cr_dict, ARMOR_CLASS_INDEX, 15) == ("7", "5")
    assert find_cr_level(cr_dict, ARMOR_CLASS_INDEX, 19) == ("30", "17")

    #Be sure it raises appropriate errors
    with pytest.raises(IndexError):
        find_cr_level(cr_dict, 20, 1)


pytest.main(["-v", "--tb=line", "-rN", __file__])
