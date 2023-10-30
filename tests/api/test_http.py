import os
import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")

@pytest.mark.http
def test_second_request():
    os.system('chcp 65001')
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['Server'] =='GitHub.com'
    print(f"Response Status code is {r.status_code}")
    print(f"Response Headers are {r.headers}")

@pytest.mark.http
def test_status_code_request():
    os.system('chcp 65001')
    r = requests.get('https://api.github.com/users/alex_morozov')
    body = r.json()
    headers = r.headers

    
    assert r.status_code == 404
    assert headers['Server'] =='GitHub.com'
    print(f"Response Status code is {r.status_code}")
    print(f"Response Headers are {r.headers}")
