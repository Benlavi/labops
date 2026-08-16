from labops import health


def test_get_status():
    assert health.get_status(0) == "OK"
    assert health.get_status(79.9) == "OK"
    assert health.get_status(80) == "WARNING"
    assert health.get_status(89.9) == "WARNING"
    assert health.get_status(90) == "CRITICAL"
    assert health.get_status(100) == "CRITICAL"