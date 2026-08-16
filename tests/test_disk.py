from labops.disk import get_disk_usage 


def test_get_disk_usage_dict_structure():
    results = get_disk_usage()
    assert isinstance(results, dict), "Result should be a dictionary."
    assert "total_gb" in results, "Missing 'total_gb' key."
    assert "used_gb" in results, "Missing 'used_gb' key."
    assert "free_gb" in results, "Missing 'free_gb' key."
    assert "percent" in results, "Missing 'percent' key."

def test_get_disk_usage_keys_names():
    results = get_disk_usage()
    expected_keys = {"total_gb", "used_gb", "free_gb", "percent"}
    assert set(results.keys()) == expected_keys, f"Keys should be {expected_keys}."

def test_get_disk_usage_values():
    results = get_disk_usage()
    assert isinstance(results["total_gb"], float), "'total_gb' should be a float."
    assert isinstance(results["used_gb"], float), "'used_gb' should be a float."
    assert isinstance(results["free_gb"], float), "'free_gb' should be a float."
    assert isinstance(results["percent"], float), "'percent' should be a float."
    


def test_get_disk_usage_values_range():
    results = get_disk_usage()
    assert results["total_gb"] > 0, "'total_gb' should be positive."
    assert results["used_gb"] >= 0, "'used_gb' should be non-negative."
    assert results["free_gb"] >= 0, "'free_gb' should be non-negative."
    assert 0 <= results["percent"] <= 100, "'percent' should be between 0 and 100."

