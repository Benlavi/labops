from labops import main

def test_get_exit_status():
    assert main.get_exit_status(None) == 0
    assert main.get_exit_status("OK") == 0
    assert main.get_exit_status("WARNING") == 1
    assert main.get_exit_status("CRITICAL") == 2
    assert main.get_exit_status("Banana") == 3