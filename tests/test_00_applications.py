from fastapi import FastAPI, ItemModel


def test_app_get_excludes_defaults() -> None:
    app = FastAPI()
    route = app.get(response_model_exclude_defaults=True)
    payload = route.render(ItemModel(enabled=True, nickname=None, priority=1, count=2))
    assert payload == {"nickname": None, "count": 2}
