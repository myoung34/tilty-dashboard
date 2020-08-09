# -*- coding: utf-8 -*-
from datetime import datetime

from tilty_dashboard.model import Tilt


def test_serialize(
):
    _tilt = Tilt()
    _tilt.timestamp = datetime.strptime('20-08-01T07:56:18', '%y-%m-%dT%H:%M:%S')
    _tilt.gravity = 1.08
    _tilt.temp = 40
    _tilt.mac = '11:22:33:44'
    _tilt.color = 'magenta'
    assert _tilt.serialize() == {
        'id': None,
        'color': 'magenta',
        'gravity': 1.08,
        'temp': 40,
        'mac': '11:22:33:44',
        'timestamp': '2020-08-01T07:56:18'
    }
