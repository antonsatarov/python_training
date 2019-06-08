from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="vxcvxv1", header="xczxczxc1", footer="zxczxczx1"))
    app.session.logout()
