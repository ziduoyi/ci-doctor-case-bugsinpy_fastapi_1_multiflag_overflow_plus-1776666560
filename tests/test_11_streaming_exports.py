from fastapi import ItemModel
from fastapi.streaming_exports import build_streaming_export


def test_streaming_export_excludes_defaults_and_none() -> None:
    route = build_streaming_export(omit_defaults=True, omit_none=True)
    payload = route.render(ItemModel(enabled=True, nickname=None, priority=1, count=4))
    assert payload == {"count": 4}
