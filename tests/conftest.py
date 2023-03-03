import pytest
from search_test_task import app, db


@pytest.fixture(scope='session')
def get_app():
    app.config.update({'TESTING': True})

    with app.app_context():
        db.metadata.create_all(bind=db.engine)

        yield app

        db.metadata.drop_all


@pytest.fixture()
def client(get_app):
    return app.test_client()
