from app.config import Settings


def test_default_settings_are_loaded() -> None:
    settings = Settings.model_validate({})

    assert settings.app_name == "OpsPilot AI"
    assert settings.app_env == "local"
    assert settings.app_debug is False
