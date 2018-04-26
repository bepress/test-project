

def test_test():
    assert True


def test_db(admin_user):
    assert admin_user.pk
