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


def test_device_config(
    client
):
    """Test that the device config works."""

    with mock.patch("builtins.open", mock.mock_open(read_data=b'data')) as mock_file:
        assert client.get(url_for('device_config')).status_code == 200
        assert mock_file.mock_calls[0] == mock.call('/etc/tilty/tilty.ini', 'r')


def test_dashboard_settings(client):
    """Test that the dashboard settings works."""

    assert client.get(url_for('dashboard_settings')).status_code == 200


def test_save_device_config(
    app,
):
    with mock.patch("builtins.open", mock.mock_open(read_data=b'data')) as mock_file:
        test_client = app.test_client()
        socketio_test_client = socketio.test_client(
            app,
            flask_test_client=test_client
        )

        assert socketio_test_client.is_connected()
        assert test_client.get(url_for('index')).status_code == 200
        socketio_test_client.emit(
            'save device config',
            {
                'data': {
                    'config': 'foo',
                }
            }
        )
        assert socketio_test_client.get_received() == []


def test_save_settings(
    app,
):
    test_client = app.test_client()
    socketio_test_client = socketio.test_client(
        app,
        flask_test_client=test_client
    )

    assert socketio_test_client.is_connected()
    assert test_client.get(url_for('index')).status_code == 200
    socketio_test_client.emit(
        'save dashboard settings',
        {
            'settings': {
                'gravity_meas': 'Brix',
                'gravity_offset': '',
                'temp_meas': 'Fahrenheit',
            }
        }
    )
    assert socketio_test_client.get_received() == []


def test_refresh(
    app,
):
    test_client = app.test_client()
    socketio_test_client = socketio.test_client(
        app,
        flask_test_client=test_client
    )

    assert socketio_test_client.is_connected()
    assert test_client.get(url_for('index')).status_code == 200
    socketio_test_client.emit('refresh')
    assert socketio_test_client.get_received() == [
        {
            'name': 'refresh',
            'args': [{
                'data': [],
            }],
            'namespace': '/'
        }
    ]

def test_logs(
    app,
):
    test_client = app.test_client()
    socketio_test_client = socketio.test_client(
        app,
        flask_test_client=test_client
    )

    with mock.patch("builtins.open", mock.mock_open(read_data=b"data")) as mock_file:
        assert socketio_test_client.is_connected()
        assert test_client.get(url_for('logs')).status_code == 200
        socketio_test_client.emit('logs')
        assert socketio_test_client.get_received() == [
            {
                'name': 'logs',
                'args': [{'data': b'data'}],
                'namespace': '/'
            }
        ]
