import json
import time
from pathlib import Path
import os


class Config:
    """Handles configuration for candidate and job profile settings, including assessments."""

    def __init__(self, assessment_id: str = None, job_profile_text: str = None):
        self.base_path = Path(__file__).parent
        self.assessment_id = assessment_id

        # Get the environment var
        self.environment = os.getenv("SELF_ASSESSMENT_APP_ENVIRONMENT", "dev")
        # Paths for the candidate configuration
        self.candidate_config_path = self.base_path / "assets/docs/candidate/candidate.json"

        # Handle three main scenarios
        if self.assessment_id:
            self.config = self._load_existing_config()
        elif job_profile_text:
            self.assessment_id = self._generate_assessment_id()
            self.config = self._create_new_assessment_config(job_profile_text)
        else:
            raise ValueError("Either assessment_id or job_profile_text must be provided.")

    @staticmethod
    def _generate_assessment_id():
        """Generate a unique assessment ID using a timestamp."""
        return str(int(time.time()))

    def _get_assessment_folder(self):
        """Return the folder path for the current assessment."""
        return self.base_path / f"assets/docs/assessments/{self.assessment_id}"

    def _get_config_path(self):
        """Return the path to the configuration file for the current assessment."""
        return self._get_assessment_folder() / "config.json"

    def _load_existing_config(self):
        """Load configuration for an existing assessment, handling missing files gracefully."""
        config_path = self._get_config_path()

        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found for assessment ID: {self.assessment_id}")

        with open(self.candidate_config_path, "r") as f:
            candidate_config = json.load(f)

        with open(config_path, "r") as f:
            assessment_config = json.load(f)

        # Merge configs, prioritizing assessment_config
        return self._merge_configs(candidate_config, assessment_config)

    def _create_new_assessment_config(self, job_profile_text):
        """Create a new assessment configuration and save the job profile text."""
        assessment_folder = self._get_assessment_folder()
        assessment_folder.mkdir(parents=True, exist_ok=True)

        # Define the file paths for the new assessment
        config_content = {
            "assessment_id": self.assessment_id,
            "job_profile_file": str(assessment_folder / "job_profile.md"),
            "cover_letter_file": str(assessment_folder / "cover_letter.md"),
            "requirements_assessment_file": str(assessment_folder / "requirements_assessment.json")
        }

        # Save the job profile text
        with open(config_content["job_profile_file"], "w") as f:
            f.write(job_profile_text)

        # Save the new configuration
        config_path = self._get_config_path()
        with open(config_path, "w") as f:
            json.dump(config_content, f, indent=4)

        # Load and merge with the candidate config
        with open(self.candidate_config_path, "r") as f:
            candidate_config = json.load(f)

        return self._merge_configs(candidate_config, config_content)

    def _merge_configs(self, candidate_config, assessment_config):
        """Merge candidate and assessment configurations, with assessment_config taking precedence."""
        combined_config = {**candidate_config, **assessment_config}

        # Adjust paths to be absolute
        for key, value in combined_config.items():
            if isinstance(value, str) and "assets/" in value:
                combined_config[key] = str(self.base_path / value)

        combined_config["environment"] = self.environment

        return combined_config

    def __setitem__(self, key, value):
        """Set a key-value pair in the configuration and save the updated config immediately.

        Args:
            key (str): The key for the configuration entry.
            value: The value for the configuration entry.
        """
        # Set the key-value pair in the configuration
        self.config[key] = value

        # Save the updated configuration to the config.json file
        config_path = self._get_config_path()
        with open(config_path, "w") as f:
            json.dump(self.config, f, indent=4)

        print(f"Updated '{key}: {value}' in config and saved to {config_path}")

    def get(self, key, default=None):
        """Retrieve a configuration value by key with an optional default."""
        return self.config.get(key, default)

    def __getitem__(self, key):
        """Enable dict-style access to configuration keys."""
        return self.config[key]
