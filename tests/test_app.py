# -*- coding: utf-8 -*-
import json
import uuid

from flask import url_for
from pytest_flask.fixtures import client


def test_app(app):
    """Test to make sure the app is loading properly."""

    assert app


def test_index(client):
    """Test that the index works."""

    assert client.get(url_for('index')).status_code == 200
