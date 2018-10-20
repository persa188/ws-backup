#!/usr/bin/env python3
import os, shutil

from time import strftime

# CONSTS && VARS
BACKUP_BASE_DIR = "bak-test/"
FOLLOW_SYMLINKS = False
IGNORED_PATTERNS = ("*.txt",)
SRC_DIR = "src-test"
TIME_TEMPLATE = "%Y-%m-%d_%H:%M:%S"

def do_backup():
    backup_dir = BACKUP_BASE_DIR + strftime(TIME_TEMPLATE)
    shutil.copytree(SRC_DIR, backup_dir,
                    symlinks=FOLLOW_SYMLINKS,
                    ignore=shutil.ignore_patterns(*IGNORED_PATTERNS))
    return backup_dir

print(os.listdir(do_backup()))
