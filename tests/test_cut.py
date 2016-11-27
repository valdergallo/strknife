# encoding: utf-8
from strknife import Cut, Knife

name = Cut(size=10, value='name')
address = Cut(size=25, value='address')


class myKnife(Knife):
    name = name
    address = address


def test_get_cuts():
    my_knife = myKnife()
    assert my_knife._cuts() == [name, address]


def test_fill_values():
    source = 'Cut Test  ' + 'Next position address    '
    my_knife = myKnife(source)
    my_knife.crop_lines()

    assert my_knife.name.value == 'Cut Test  '
    assert my_knife.address.value == 'Next position address    '


def test_fill_values_any_chars():
    source = u'Cut Test  ' + u'Next_çã%&a-address~*@!'
    my_knife = myKnife(source)
    my_knife.crop_lines()

    assert my_knife.name.value == 'Cut Test  '
    assert my_knife.address.value == u'Next_çã%&a-address~*@!'
