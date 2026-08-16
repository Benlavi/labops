import pytest
from labops.disk import get_disk_usage 


@pytest.fixture
def disk_usage_results():
    return get_disk_usage()

def test_get_disk_usage_dict_structure(disk_usage_results):
    assert isinstance(disk_usage_results, dict), "Result should be a dictionary."
    assert "total_gb" in disk_usage_results, "Missing 'total_gb' key."
    assert "used_gb" in disk_usage_results, "Missing 'used_gb' key."
    assert "free_gb" in disk_usage_results, "Missing 'free_gb' key."
    assert "percent" in disk_usage_results, "Missing 'percent' key."

def test_get_disk_usage_keys_names(disk_usage_results):
    expected_keys = {"total_gb", "used_gb", "free_gb", "percent"}
    assert set(disk_usage_results.keys()) == expected_keys, f"Keys should be {expected_keys}."

def test_get_disk_usage_values(disk_usage_results):
    assert isinstance(disk_usage_results["total_gb"], float), "'total_gb' should be a float."
    assert isinstance(disk_usage_results["used_gb"], float), "'used_gb' should be a float."
    assert isinstance(disk_usage_results["free_gb"], float), "'free_gb' should be a float."
    assert isinstance(disk_usage_results["percent"], float), "'percent' should be a float."
    

def test_get_disk_usage_values_range(disk_usage_results):
    
    assert disk_usage_results["total_gb"] > 0, "'total_gb' should be positive."
    assert disk_usage_results["used_gb"] >= 0, "'used_gb' should be non-negative."
    assert disk_usage_results["free_gb"] >= 0, "'free_gb' should be non-negative."
    assert 0 <= disk_usage_results["percent"] <= 100, "'percent' should be between 0 and 100."

