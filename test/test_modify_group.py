from model.group import Group


def test_modify_name(app):
    app.group.modify_first_group(Group(name="New Group"))


def test_modify_header(app):
    app.group.modify_first_group(Group(header="New Header"))