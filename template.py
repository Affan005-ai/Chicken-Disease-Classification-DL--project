from pathlib import Path
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


PROJECT_NAME = "cnn_classifier_1"


FILES_TO_CREATE = [
    Path(".github/workflows/.gitkeep"),
    Path(f"src/{PROJECT_NAME}/__init__.py"),
    Path(f"src/{PROJECT_NAME}/components/__init__.py"),
    Path(f"src/{PROJECT_NAME}/utils/__init__.py"),
    Path(f"src/{PROJECT_NAME}/config/__init__.py"),
    Path(f"src/{PROJECT_NAME}/config/configuration.py"),
    Path(f"src/{PROJECT_NAME}/pipeline/__init__.py"),
    Path(f"src/{PROJECT_NAME}/entity/__init__.py"),
    Path(f"src/{PROJECT_NAME}/constants/__init__.py"),
    Path("config/config.yaml"),
    Path("dvc.yaml"),
    Path("params.yaml"),
    Path("pyproject.toml"),
    Path("requirements.txt"),
    Path("research/trials.ipynb"),
]


def create_project_structure() -> None:
    for filepath in FILES_TO_CREATE:
        if filepath.parent != Path("."):
            filepath.parent.mkdir(parents=True, exist_ok=True)
            logging.info("Ensured directory exists: %s", filepath.parent)

        if not filepath.exists():
            filepath.touch()
            logging.info("Created file: %s", filepath)
        else:
            logging.info("File already exists: %s", filepath)


def main() -> None:
    create_project_structure()


if __name__ == "__main__":
    main()


   

