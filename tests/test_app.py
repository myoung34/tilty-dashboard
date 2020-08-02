# -*- coding: utf-8 -*-
import json
import uuid
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


def test_refresh_no_data(
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
            'args': [{'data': 'n/a'}],
            'namespace': '/'
        }
    ]



class mock_tilt_reading:
    def __init__(self):
        self.gravity = 1000
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
            'args': [{'data': 1000}],
            'namespace': '/'
        }
    ]
