from fastapi import ItemModel
from fastapi.integrations.regional_alias_feed import build_regional_alias_feed


def test_regional_alias_feed_combines_aliases_defaults_and_none() -> None:
    route = build_regional_alias_feed(trim_defaults=True, trim_none=True, external_names=True)
    payload = route.render(ItemModel(enabled=True, nickname=None, priority=1, count=8))
    assert payload == {"itemCount": 8}
