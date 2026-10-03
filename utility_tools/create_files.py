#!/usr/bin/env python

"""
This script helps in creating files under specific directory using argument 

"""

import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("folder")
parser.add_argument("filename")
args = parser.parse_args()

folder = Path(args.folder)
if not folder.is_dir():
    parser.error(f"Folder does not exist: {folder}")

file_path = folder / args.filename
file_path.touch()
print(f"Created: {file_path}")