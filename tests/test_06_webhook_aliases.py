from fastapi import ItemModel, build_webhook


def test_webhook_uses_aliases_and_excludes_defaults() -> None:
    route = build_webhook(strip_defaults=True, use_aliases=True)
    payload = route.render(ItemModel(enabled=True, nickname=None, priority=1, count=2))
    assert payload == {"nickName": None, "itemCount": 2}
