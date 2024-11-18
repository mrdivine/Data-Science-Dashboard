from pathlib import Path
import re
import json


def save_to_file(filename: str, content: str):
    with open(filename, "w") as f:
        f.write(content)


def read_csv_as_string(file_path: str) -> str:
    """Read a CSV file and return its contents as a string."""
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, "r") as f:
        return f.read()


def parse_executive_summary(filepath: str) -> str:
    """Extract the executive summary from a markdown file based on heading."""
    with open(filepath, "r") as file:
        content = file.read()

    # Extract text under the 'Executive Summary' heading
    match = re.search(r"## Executive Summary\n(.+?)(\n## |$)", content, re.DOTALL)
    return match.group(1).strip() if match else ""


def load_json(json_file_path):
    """Load the structured output from a JSON file."""
    with open(json_file_path, "r") as json_file:
        requirements_data = json.load(json_file)
    # Verify by printing the contents (optional)
    return requirements_data