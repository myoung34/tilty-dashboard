# -*- coding: utf-8 -*-
import json
import uuid
from datetime import datetime
from unittest import mock

from flask import url_for
from pytest_flask.fixtures import client

from tilty_dashboard import socketio


def test_app(app):
    """Test to make sure the app is loading properly."""

    assert app


def test_index(client):
    """Test that the index works."""

    assert client.get(url_for('index')).status_code == 200


@mock.patch('tilty_dashboard.datetime')
def test_refresh_no_data(
    mock_time,
    client,
    app,
):
    socketio_test_client = socketio.test_client(
        app, flask_test_client=client)

    assert socketio_test_client.is_connected()
    assert client.get(url_for('index')).status_code == 200
    socketio_test_client.emit('refresh')
    assert socketio_test_client.get_received() == [
        {
            'name': 'refresh',
            'args': [{
                'data': {
                    'color': 'n/a',
                    'gravity': 0,
                    'mac': '',
                    'temp': 0,
                    'timestamp': mock.ANY
                }
            }],
            'namespace': '/'
        }
    ]



class mock_tilt_reading:
    def __init__(self):
        self.gravity = 1000
        self.temp = 66
        self.color = 'black'
        self.mac = '00:11:22:33:44'
        self.timestamp = datetime.strptime('20-08-03T07:56:18', '%y-%m-%dT%H:%M:%S')
class mock_tilt_item:
    def __init__(self):
        return None
    def first():
        return mock_tilt_reading()
class mock_tilt_model:
    class timestamp:
        def __init__(self):
            return None
    class query:
        def order_by(item):
            return mock_tilt_item


@mock.patch(
    'tilty_dashboard.Tilt',
    new=mock_tilt_model,
)
@mock.patch('tilty_dashboard.sqlalchemy.desc')
def test_refresh(
    mock_desc,
    client,
    app,
):
    socketio_test_client = socketio.test_client(
        app, flask_test_client=client)

    assert socketio_test_client.is_connected()
    assert client.get(url_for('index')).status_code == 200
    socketio_test_client.emit('refresh')
    mock_desc.mock_calls == [
        mock.call(mock.ANY)
    ]
    assert socketio_test_client.get_received() == [
        {
            'name': 'refresh',
            'args': [{
                'data': {
                    'color': 'black',
                    'gravity': 1000,
                    'mac': '00:11:22:33:44',
                    'temp': 66,
                    'timestamp': '2020-08-03T07:56:18',
                }
            }],
            'namespace': '/'
        }
    ]
