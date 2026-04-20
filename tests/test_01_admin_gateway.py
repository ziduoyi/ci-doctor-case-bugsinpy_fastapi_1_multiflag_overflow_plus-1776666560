from fastapi import AdminGateway, ItemModel


def test_admin_list_excludes_defaults() -> None:
    route = AdminGateway().list(hide_defaults=True)
    payload = route.render(ItemModel(enabled=True, nickname=None, priority=1, count=2))
    assert payload == {"nickname": None, "count": 2}
