import json
import os
import tempfile
import pytest
import scrap_cacher

port = os.environ.get("PORT", 8000)

@pytest.fixture
def client():
    scrap_cacher.app.config['TESTING'] = True
    client = scrap_cacher.app.test_client()
    yield client

def test_check_health(client):
    #test health check
	rv = client.get('/health')
	assert b'healthy' in rv.data

def test_post_key_value(client):
    #test normal save operation
    res = client.post('/save',
                      json = {"key" : "key1", "value" : "value1"},
                      follow_redirects = True)
    print(res.data, res)
    assert res.status_code == 200
    assert json.loads(res.data.decode()) == {"errors":"", "result" : "saved"}

def test_get_value(client):
    #test normal get operation
    res = client.get('/get/key1')
    print(res.data, res)
    assert res.status_code == 200
    assert json.loads(res.data.decode()) == {"errors":"", "result" : "value1"}
    res = client.get('/get/key11')
    assert res.status_code == 400
    assert json.loads(res.data.decode()) == {"errors":"invalid key", "result" : None}

def test_check_health(client):
    #test normal get operation
    res = client.get('/health')
    print(res.data, res)
    assert res.status_code == 200
    assert json.loads(res.data.decode()) == {"errors":"", "result" : "healthy"}
