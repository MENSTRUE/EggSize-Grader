from fastapi.testclient import TestClient
from backend.app.main import app

client=TestClient(app)
def test_health():
    r=client.get('/api/v1/health')
    assert r.status_code==200
    assert r.json()['status']=='ok'

def test_model_contract():
    r=client.get('/api/v1/model')
    assert r.status_code==200
    assert r.json()['classes']==['large','medium','small']

def test_invalid_type():
    r=client.post('/api/v1/predict',files={'file':('file.txt',b'hello','text/plain')})
    assert r.status_code==415

def test_invalid_image():
    r=client.post('/api/v1/predict',files={'file':('bad.png',b'not an image','image/png')})
    assert r.status_code==422
