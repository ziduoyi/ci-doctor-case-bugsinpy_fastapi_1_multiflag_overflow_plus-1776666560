from fastapi import FastAPI, ItemModel


def test_post_route_uses_aliases() -> None:
    app = FastAPI()
    route = app.post(response_model_by_alias=True)
    payload = route.render(ItemModel(enabled=False, nickname="neo", priority=3, count=2))
    assert payload == {
        "enabled": False,
        "nickName": "neo",
        "priority": 3,
        "itemCount": 2,
    }
