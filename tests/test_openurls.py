import os
import pytest
import bdauth


@pytest.fixture
def client():
    os.environ['FLASK_ENV'] = 'testing'
    with bdauth.app.test_client() as client:
        yield client


def test_isbn(client):
    response = client.get('/openurl/?rft.isbn=978-3-16-148410-0')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query=isbn%3D%22978-3-16-148410-0%22'
    assert response.headers['location'] == expected


def test_title_no_author(client):
    response = client.get('/openurl/?rft.title=title')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query=ti%3D%22title%22'
    assert response.headers['location'] == expected


def test_title_with_author(client):
    response = client.get('/openurl/?rft.title=title&rft.aulast=last')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query=ti%3D%22title%22%20and%20au%3D%22last%22'
    assert response.headers['location'] == expected


def test_btitle_no_author(client):
    response = client.get('/openurl/?rft.btitle=title')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query=ti%3D%22title%22'
    assert response.headers['location'] == expected


def test_btitle_with_author(client):
    response = client.get('/openurl/?rft.btitle=title&rft.aulast=last')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query=ti%3D%22title%22%20and%20au%3D%22last%22'
    assert response.headers['location'] == expected


def test_ctitle_no_author(client):
    response = client.get('/openurl/?rft.btitle=title')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query=ti%3D%22title%22'
    assert response.headers['location'] == expected


def test_ctitle_with_author(client):
    response = client.get('/openurl/?rft.btitle=title&rft.aulast=last')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query=ti%3D%22title%22%20and%20au%3D%22last%22'
    assert response.headers['location'] == expected


def test_jtitle_no_author(client):
    response = client.get('/openurl/?rft.btitle=title')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query=ti%3D%22title%22'
    assert response.headers['location'] == expected


def test_jtitle_with_author(client):
    response = client.get('/openurl/?rft.btitle=title&rft.aulast=last')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query=ti%3D%22title%22%20and%20au%3D%22last%22'
    assert response.headers['location'] == expected


def test_no_rft_fields_of_interest(client):
    response = client.get('/openurl/?rft.popcorn=soup')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query='
    assert response.headers['location'] == expected


def test_title_priority(client):
    response = client.get(
        '/openurl/?rft.title=title&rft.btitle=btitle&rft.ctitle=ctitle&rft.jtitle=jtitle&rft.aulast=last')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query=ti%3D%22title%22%20and%20au%3D%22last%22'
    assert response.headers['location'] == expected


def test_btitle_priority(client):
    response = client.get(
        '/openurl/?rft.btitle=btitle&rft.ctitle=ctitle&rft.jtitle=jtitle&rft.aulast=last')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query=ti%3D%22btitle%22%20and%20au%3D%22last%22'
    assert response.headers['location'] == expected


def test_ctitle_priority(client):
    response = client.get(
        '/openurl/?rft.ctitle=ctitle&rft.jtitle=jtitle&rft.aulast=last')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query=ti%3D%22ctitle%22%20and%20au%3D%22last%22'
    assert response.headers['location'] == expected


def test_jtitle_priority(client):
    response = client.get(
        '/openurl/?rft.jtitle=jtitle&rft.aulast=last')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query=ti%3D%22jtitle%22%20and%20au%3D%22last%22'
    assert response.headers['location'] == expected


def test_fields_of_no_interest_ignored(client):
    response = client.get(
        '/openurl/?rft.isbn=978-3-16-148410-0&rft.popcorn=soup')
    assert response.status_code == 307
    expected = 'http://example.com/?LS=XYZ&PI=yo@example.com&query=isbn%3D%22978-3-16-148410-0%22'
    assert response.headers['location'] == expected
