import argparse
import time

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    "--database-file-path",
    required = True,
    help="path to sqlite database file"
  )
  parser.add_argument(
    "--host",
    default="0.0.0.0",
    help="ip address server listens on, default is 0.0.0.0"
  )
  parser.add_argument(
    "--port",
    type=int,
    default=8000,
    help="port for the server to be hosted on, default is 8000"
  )

  return parser.parse_args()