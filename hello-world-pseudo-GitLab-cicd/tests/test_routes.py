from app.routes import app

def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "Hello, World!"