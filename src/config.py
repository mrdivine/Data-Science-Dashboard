import json
import re
from pathlib import Path


class Config:
    """Handles configuration for candidate and job profile settings."""

    def __init__(self, profile_title: str, job_profile_text: str = None, candidate_config_path: str = None):
        self.base_path = Path(__file__).parent
        if not candidate_config_path:
            candidate_config_path = self.base_path / "assets/config/candidate.json"

        if job_profile_text:
            profile_config_path = self.create_profile_config(profile_title, job_profile_text)

        else:
            profile_title, profile_config_path = self.get_profile_config_path(profile_title)

        self.config = self._load_config(candidate_config_path, profile_config_path)

    def get_profile_config_path(self, profile_title: str):
        safe_title = self._sanitize_title(profile_title)
        return safe_title, f"{self.base_path}/assets/config/{safe_title}.json"

    def create_profile_config(self, profile_title, job_profile_text):
        """Creates a configuration JSON file for a given profile title if it doesn't exist.

        :param profile_title: Title of the profile (e.g., 'Business Analyst').
        :return: Path to the newly created profile configuration file.
        """
        # Make title filesystem-safe
        safe_title, profile_config_path = self.get_profile_config_path(profile_title)

        # Define the file paths for output files based on title
        config_content = {
            "profile_title": f"{profile_title}",
            "job_profile_file": f"assets/docs/input/{safe_title}/{safe_title}_job_profile.md",
            "cover_letter_file": f"assets/docs/output/{safe_title}/{safe_title}_cover_letter.md",
            "job_profile_skills_file": f"assets/docs/output/{safe_title}/{safe_title}_job_profile_skills.csv",
            "candidate_skills_file": f"assets/docs/output/{safe_title}/{safe_title}_candidate_skills.csv",
            "requirements_assessment_file": f"assets/docs/output/{safe_title}/{safe_title}_requirements_assessment.csv"
        }
        # Ensure each directory in the config exists
        for key, filepath in config_content.items():
            # Skip 'profile_title' as it’s not a path
            if key == "profile_title":
                continue

            # Extract directory path and create if it doesn’t exist
            directory = Path(filepath).parent
            directory.mkdir(parents=True, exist_ok=True)

        # Save the initial config if it doesn't already exist
        config_path = Path(profile_config_path)

        if not config_path.exists():
            with open(config_path, "w") as f:
                json.dump(config_content, f, indent=4)
            print(f"Created new profile config at {profile_config_path}")

        with open(config_content["job_profile_file"], "w") as f:
            f.write(job_profile_text)

        return profile_config_path

    @staticmethod
    def _sanitize_title(title):
        """Sanitizes a title to be filesystem-safe."""
        return re.sub(r'[^\w\s-]', '', title).replace(" ", "_")

    def _load_config(self, candidate_config_path, profile_config_path):
        """Loads and merges candidate and profile configurations."""
        # Read candidate config
        with open(candidate_config_path, "r") as f:
            candidate_config = json.load(f)

        # Read profile config
        with open(profile_config_path, "r") as f:
            profile_config = json.load(f)

        # Merge configs with profile_config overriding candidate_config on conflicts
        combined_config = {**candidate_config, **profile_config}

        # Add base path to all path entries in the config
        for key, value in combined_config.items():
            if isinstance(value, str) and "assets/" in value:  # Adjust for all paths in assets folder
                combined_config[key] = str(self.base_path / value)

        return combined_config

    def get(self, key, default=None):
        """Retrieve a configuration value by key with an optional default."""
        return self.config.get(key, default)

    def __getitem__(self, key):
        """Enable dict-style access to configuration keys."""
        return self.config[key]
