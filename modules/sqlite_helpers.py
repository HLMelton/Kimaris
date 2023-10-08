import sqlite3
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

def maybe_create_table(sqlite_file: str) -> bool:
  db = sqlite3.connect(sqlite_file)
  cursor = db.cursor()

  try:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY, 
        uid TEXT NOT NULL, 
        created_at DATETIME NOT NULL);
    """

    create_index_query = """
    CREATE UNIQUE INDEX IF NOT EXISTS idx_urls_alias
    ON urls (alias);
    """

    cursor.execute(create_table_query)
    cursor.execute(create_index_query)
    db.commit()
    return True
  except Exception:
    logger.exception("Unable to create uid table")
    return False
    
def insert_uid(sqlite_file: str, uid: str):
  db = sqlite3.connect(sqlite_file)
  cursor = db.cursor()
  timestamp = datetime.now()

  try: 
    sql = "INSERT INTO uids(uid, created_at) VALUES (?,?)"
    val = (uid, timestamp)
    cursor.execute(sql, val)
    db.commit()
    return True
  except sqlite3.IntegrityError:
    return False
  except Exception:
    logger.exception("Inserting url had an error")
    return False

def remove_uid(sqlite_file: str, uid: str):
  db = sqlite3.connect(sqlite_file)
  cursor = db.cursor()

  try:
    sql = "DELETE FROM uids WHERE uid = ?"
    cursor.execute(sql, (uid, ))
    db.commit()

    return cursor.rowcount > 0
  except Exception:
      logger.exception("Deleting url had an error")
      return False

def get_uids(sqlite_file: str): #returns all udis registered

  db = sqlite3.connect(sqlite_file)
  cursor = db.cursor()

  sql = "SELECT * FROM uids"
  cursor.execute(sql)
  result = cursor.fetchall()
  uid_array = []
  for row in result:
    try:
      uid_data = {
        "id": row[0],
        "uid": row[1],
        "created_at": row[2],
      }
      uid_array.append(uid_data)
    except KeyError:
      continue
  return uid_array

def get_number_of_uris(sqlite_file: str):
  db = sqlite3.connect(sqlite_file)
  cursor = db.cursor()

  count = 0
  try:
    sql = "SELECT COUNT(*) from uris"
    cursor.execute(sql)
    result = cursor.fetchone()
    count = result[0]
  except Exception:
    logger.exception("Couldn't get number of urls")
  return count
