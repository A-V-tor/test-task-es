import random


def test_delete(client):
    id = random.randint(1, 1500)
    res = client.delete(f'/remove/{id}/')

    assert res.status_code == 200


def test_search(client):
    value = random.choice(
        ['привет', 'как дела', 'танцы', 'рост', 'о себе не много']
    )
    res = client.get(f'/search/{value}/')

    assert res.status_code == 200
