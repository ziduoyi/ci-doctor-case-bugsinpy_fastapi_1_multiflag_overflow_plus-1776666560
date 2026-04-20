from fastapi import ItemModel, schedule_job


def test_background_job_uses_aliases() -> None:
    route = schedule_job(alias_output=True)
    payload = route.render(ItemModel(enabled=False, nickname="job", priority=3, count=5))
    assert payload == {
        "enabled": False,
        "nickName": "job",
        "priority": 3,
        "itemCount": 5,
    }
