from stellar_forge.models import ModelSpec


def test_table_name(user_class):
    m = ModelSpec(user_class)

    assert m.table() == "test_user"
