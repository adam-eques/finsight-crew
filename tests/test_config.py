import textwrap

from finsight.config import Settings, load_settings


def test_defaults(tmp_path):
    s = load_settings(tmp_path / "missing.yaml")
    assert isinstance(s, Settings)
    assert s.llm_provider == "anthropic"
    assert s.temperature == 0.2


def test_yaml_is_loaded(tmp_path):
    cfg = tmp_path / "settings.yaml"
    cfg.write_text(textwrap.dedent("""
        llm_provider: openai
        temperature: 0.7
    """))
    s = load_settings(cfg)
    assert s.llm_provider == "openai"
    assert s.temperature == 0.7


def test_env_override(tmp_path, monkeypatch):
    monkeypatch.setenv("FINSIGHT_MAX_RPM", "5")
    monkeypatch.setenv("FINSIGHT_VERBOSE", "false")
    s = load_settings(tmp_path / "missing.yaml")
    assert s.max_rpm == 5
    assert s.verbose is False


def test_new_settings_defaults(tmp_path):
    s = load_settings(tmp_path / "missing.yaml")
    assert s.output_format == "md"
    assert s.save_manifest is False
