#!/usr/bin/env python3
"""Validate the package before publishing."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

from _maintainer import REPO_ROOT, SRC_DIR, python_env, regenerate_registry, resolve_python


def run(command: list[str], *, cwd: Path | None = None) -> None:
    print("$", " ".join(command))
    subprocess.run(command, check=True, cwd=cwd or REPO_ROOT, env=python_env())


def main() -> None:
    python = resolve_python()
    required_paths = [
        SRC_DIR / "address_encoder" / "py.typed",
        SRC_DIR / "address_encoder" / "__init__.py",
        SRC_DIR / "address_encoder" / "coders.py",
        REPO_ROOT / "README.md",
        REPO_ROOT / "pyproject.toml",
    ]
    missing = [path for path in required_paths if not path.exists()]
    if missing:
        raise SystemExit("Missing required publish files:\n" + "\n".join(str(path) for path in missing))

    regenerate_registry()
    run([python, "-m", "pytest", "-q"], cwd=REPO_ROOT)

    with tempfile.TemporaryDirectory() as tmp:
        dist_dir = Path(tmp) / "dist"
        run([python, "-m", "pip", "install", "build", "-q"])
        run([python, "-m", "build", "--outdir", str(dist_dir)])

    print("Pre-publish checks passed.")


if __name__ == "__main__":
    main()
