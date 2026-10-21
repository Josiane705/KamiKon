import django


def test_django_is_installed():
    assert django.VERSION[0] >= 6
