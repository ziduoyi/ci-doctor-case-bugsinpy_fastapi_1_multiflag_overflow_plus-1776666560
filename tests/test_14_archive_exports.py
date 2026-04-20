from fastapi import ItemModel
from fastapi.archive_exports import build_archive_export


def test_archive_export_excludes_defaults_and_none() -> None:
    route = build_archive_export(omit_defaults=True, omit_none=True)
    payload = route.render(ItemModel(enabled=True, nickname=None, priority=1, count=5))
    assert payload == {"count": 5}
