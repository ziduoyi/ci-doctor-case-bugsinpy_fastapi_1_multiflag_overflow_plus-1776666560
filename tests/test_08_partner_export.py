from fastapi import ItemModel
from fastapi.integrations.partner_export import build_partner_export


def test_partner_export_uses_aliases_and_excludes_defaults() -> None:
    route = build_partner_export(skip_defaults=True, external_names=True)
    payload = route.render(ItemModel(enabled=True, nickname=None, priority=1, count=6))
    assert payload == {"nickName": None, "itemCount": 6}
