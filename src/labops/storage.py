import os
import sqlite3
from labops.models import StoredReport, Report
from uuid import UUID
from datetime import datetime
from contextlib import contextmanager
from collections.abc import Generator

DB_PATH = os.environ.get("LABOPS_DB_PATH", "labops.db")

@contextmanager
def db_connection() -> Generator[sqlite3.Connection]:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    try:
        with connection:
            yield connection
    finally:
        connection.close()


def init_db():
    with db_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS reports(
                id TEXT PRIMARY KEY,
                stored_at TEXT,
                hostname TEXT,
                health TEXT, 
                report_json TEXT
            )


            '''
        )



def create_stored_report_from_db(item: sqlite3.Row) -> StoredReport:
    return StoredReport(
                id=UUID(item["id"]),
                stored_at=datetime.fromisoformat(item["stored_at"]),
                report=Report.model_validate_json(item["report_json"])
        )

def save_report(stored_report: StoredReport) -> None:

   id_text = str(stored_report.id)
   stored_at_text = stored_report.stored_at.isoformat()
   hostname_text = stored_report.report.system.hostname
   health_text = stored_report.report.health.overall_status
   report_json_text = stored_report.report.model_dump_json()

   with db_connection() as connection:
       cursor = connection.cursor()

       cursor.execute(
           '''
            INSERT INTO reports(
            id,
            stored_at,
            hostname,
            health,
            report_json
            )
            VALUES(?, ?, ?, ?, ?)
            ''',
        (id_text,
        stored_at_text,
        hostname_text,
        health_text,
        report_json_text
        )
       )




def get_reports() -> list[StoredReport]:
    report_list: list[StoredReport] = []
    with db_connection() as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM reports")
        rows = cursor.fetchall()
        for row in rows:
            report_list.append(
                create_stored_report_from_db(row)
                )
            

    return report_list

def get_report_by_uuid(report_id: UUID) -> StoredReport | None:

    with db_connection() as connection:
        cursor= connection.cursor()
        cursor.execute(
            '''
           SELECT * FROM reports WHERE id = ?
            '''
           , (str(report_id),)
        )
        item = cursor.fetchone()

    if item is None:
        return None

    report = create_stored_report_from_db(item)
    

    return report

def get_reports_by_hostname(hostname: str) -> list[StoredReport]: 

    with db_connection() as connection:
        cursor = connection.cursor()

        cursor.execute(
            '''
            SELECT * FROM reports WHERE hostname = ?
            ''',
            (hostname, )
        )
        rows = cursor.fetchall()


    report_list: list[StoredReport] = []

    for row in rows:
        report_list.append(create_stored_report_from_db(row))

    return report_list