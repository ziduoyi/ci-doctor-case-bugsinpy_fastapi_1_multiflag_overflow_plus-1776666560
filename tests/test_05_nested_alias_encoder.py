from fastapi import ContainerModel, ItemModel
from fastapi.encoders import jsonable_encoder


def test_nested_encoder_uses_aliases() -> None:
    container = ContainerModel(
        label="box",
        items=[ItemModel(enabled=False, nickname="x", priority=3, count=4)],
    )
    payload = jsonable_encoder(container, by_alias=True)
    assert payload == {
        "label": "box",
        "items": [
            {
                "enabled": False,
                "nickName": "x",
                "priority": 3,
                "itemCount": 4,
            }
        ],
    }
