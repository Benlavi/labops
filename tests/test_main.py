import sys
from labops import main, health


def test_get_exit_status():
    assert main.get_exit_status(None) == 0
    assert main.get_exit_status("OK") == 0
    assert main.get_exit_status("WARNING") == 1
    assert main.get_exit_status("CRITICAL") == 2
    assert main.get_exit_status("Banana") == 3


def test_main_return_error_code_when_health_fails(monkeypatch, caplog):
    mock_args = ['labops', 'health']
    monkeypatch.setattr(sys, "argv", mock_args)

    def mock_system_health():
        raise RuntimeError("Failed to get data")
    
    monkeypatch.setattr(
        health,
        "get_system_health",
        mock_system_health
        )
    
    return_value = main.main()

    assert return_value == 3
    assert "Failed to collect system health" in caplog.text
    assert "Failed to get data" in caplog.text

   