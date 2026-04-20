from fastapi import ItemModel, MountedApp


def test_mounted_patch_excludes_none() -> None:
    route = MountedApp().patch(trim_none=True)
    payload = route.render(ItemModel(enabled=True, nickname=None, priority=1, count=2))
    assert payload == {"enabled": True, "priority": 1, "count": 2}
