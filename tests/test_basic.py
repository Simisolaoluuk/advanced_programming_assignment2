import pytest
from app import create_app
from models import db, Status, Company

@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    with app.app_context():
        db.create_all()
        s = Status(status_name="Active")
        db.session.add(s)
        db.session.commit()
        c = Company(name="Test Ltd", number="0001", postcode="AB10", status_id=s.id)
        db.session.add(c)
        db.session.commit()
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    r = client.get("/")
    assert r.status_code == 200

def test_companies(client):
    r = client.get("/companies")
    assert r.status_code == 200

def test_company_detail(client):
    r = client.get("/companies/1")
    assert r.status_code == 200
