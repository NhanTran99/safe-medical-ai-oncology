"""Baseline test: configuration loads safely without secrets/.env present."""

from safe_medical_ai.config import Settings, get_settings


def test_settings_load_with_defaults(monkeypatch, tmp_path):
    # Ensure no ambient SMA_ env vars leak into the test and no .env file
    # in the current working directory is picked up.
    for key in list(__import__("os").environ):
        if key.startswith("SMA_"):
            monkeypatch.delenv(key, raising=False)
    monkeypatch.chdir(tmp_path)

    settings = Settings()

    assert settings.app_name == "safe-medical-ai-oncology"
    assert settings.environment == "development"
    assert settings.log_level == "INFO"
    assert settings.database_url is None


def test_get_settings_is_cached():
    assert get_settings() is get_settings()


def test_settings_reads_env_prefix(monkeypatch):
    monkeypatch.setenv("SMA_APP_NAME", "override-name")
    settings = Settings()
    assert settings.app_name == "override-name"
