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


def test_index(client):
    """Test that the settings works."""

    assert client.get(url_for('settings')).status_code == 200


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
        'save settings',
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
