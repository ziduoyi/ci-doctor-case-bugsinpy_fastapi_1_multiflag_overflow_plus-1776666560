from fastapi import ItemModel
from fastapi.integrations.audit_feed import build_audit_feed


def test_audit_feed_omits_none_values() -> None:
    route = build_audit_feed(omit_missing=True)
    payload = route.render(ItemModel(enabled=True, nickname=None, priority=1, count=3))
    assert payload == {"enabled": True, "priority": 1, "count": 3}
