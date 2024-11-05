import json
import pandas as pd
from pathlib import Path
import re
import json


def save_to_file(filename: str, content: str):
    with open(filename, "w") as f:
        f.write(content)


def save_csv(filename: str, data: pd.DataFrame):
    data.to_csv(filename, index=False)


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


def read_and_clean_csv(filepath)-> pd.DataFrame:
    # Step 1: Read the CSV file
    df = pd.read_csv(filepath)

    # Step 2: Clean up column names (snake_case, lowercase)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Step 3: Convert numerical columns to strings and format the 'rating' column
    if 'rating' in df.columns:
        df = format_ratings(df)

    if 'self_assessment_score' in df.columns:
        df = format_self_assessment_score(df)

    # Step 4: Remove duplicates in the 'skill_name' column
    if 'skill_name' in df.columns:
        df = df.drop_duplicates(subset='skill_name')

    return df


def format_self_assessment_score(data):
    # Format the 'rating' column to show as an integer if whole, otherwise one decimal place
    data['self_assessment_score'] = data['self_assessment_score'].apply(
        lambda x: f"{x:.1f}".rstrip('0').rstrip('.') if isinstance(x, float) else str(x))
    return data


def format_ratings(data):
    # Format the 'rating' column to show as an integer if whole, otherwise one decimal place
    data['rating'] = data['rating'].apply(
        lambda x: f"{x:.1f}".rstrip('0').rstrip('.') if isinstance(x, float) else str(x))
    return data


def load_json(json_file_path):
    """Load the structured output from a JSON file."""
    with open(json_file_path, "r") as json_file:
        requirements_data = json.load(json_file)
    # Verify by printing the contents (optional)
    return requirements_data