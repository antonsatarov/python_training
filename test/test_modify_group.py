from model.group import Group
from random import randrange


def test_modify_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New Group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New Header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)