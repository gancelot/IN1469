"""
        files.py -      Provides the copy_files() function which returns a
                        list of duplicate files.
"""
import filecmp
import shutil
from pathlib import Path


def copy_files(src: str | Path, dst: str | Path) -> list[str]:
    files_copied = []
    src = Path(src)
    dst = Path(dst)
    if not dst.exists():
        dst.mkdir()

    to_copy = filecmp.dircmp(src, dst).left_only

    for filename in to_copy:
        shutil.copy2(src / filename, dst)
        files_copied.append(filename)

    return files_copied


def delete_common(src: str | Path, dst: str | Path) -> list[str]:
    files_deleted = []
    src = Path(src)
    dst = Path(dst)

    to_delete = filecmp.dircmp(src, dst).common

    for filename in to_delete:
        (dst / filename).unlink()
        files_deleted.append(filename)

    return files_deleted
