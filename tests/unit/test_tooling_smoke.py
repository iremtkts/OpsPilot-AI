import sys
import tomllib
from pathlib import Path

PROJECT_ROOT = Path(__file__).parents[2]


def test_project_uses_python_312() -> None:
    assert sys.version_info[:2] == (3, 12)


def test_project_metadata_and_tooling_files_exist() -> None:
    pyproject_path = PROJECT_ROOT / "pyproject.toml"
    metadata = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

    assert metadata["project"]["name"] == "opspilot-ai"
    assert metadata["project"]["version"] == "0.1.0"

    required_files = {
        ".env.example",
        ".gitignore",
        ".pre-commit-config.yaml",
        ".python-version",
        "Makefile",
        "uv.lock",
    }
    assert all((PROJECT_ROOT / path).is_file() for path in required_files)
