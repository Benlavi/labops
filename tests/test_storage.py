from labops import storage
import labops.models
from uuid import uuid4
from datetime import datetime , UTC
import pytest

@pytest.fixture
def test_database(tmp_path,monkeypatch):
    test_db = tmp_path / "test.db"
    monkeypatch.setattr(storage,"DB_PATH",test_db)
    storage.init_db()

def test_load_and_save_storage(test_database):

    stored_report = labops.models.StoredReport(
        id=uuid4(),
        stored_at= datetime.now(UTC),
        report=labops.models.Report
        (
            system=labops.models.SystemInfo(
                hostname="test",
                os_name="macos",
                kernel_version="7.0.0",
                uptime_seconds=30.0
            ),
            disk= labops.models.DiskInfo(
                total_gb=300,
                used_gb=200,
                free_gb=100,
                percent=33
            ),
            network= {},
            health=labops.models.HealthInfo(
                memory_percent=70,
                disk_percent=70,
                memory_status="OK",
                disk_status="OK",
                overall_status="OK"
            )
        )
    )

    storage.save_report(stored_report)
    loaded_report = storage.get_report_by_uuid(stored_report.id)

    assert loaded_report == stored_report


def test_get_report_by_uuid_not_found(test_database):
    assert storage.get_report_by_uuid(uuid4()) is None