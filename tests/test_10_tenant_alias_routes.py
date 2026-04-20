from fastapi import ItemModel
from fastapi.tenant_alias_routes import build_tenant_alias_route


def test_tenant_alias_route_uses_aliases_and_excludes_defaults() -> None:
    route = build_tenant_alias_route(trim_defaults=True, alias_output=True)
    payload = route.render(ItemModel(enabled=True, nickname=None, priority=1, count=9))
    assert payload == {"nickName": None, "itemCount": 9}
