from config import (
    PROVIDER_PRESETS, CHARS_PER_TOKEN, DEFAULT_TEMPERATURE,
    DEFAULT_MAX_TOKENS, DEFAULT_PORT, CONTEXT_RESERVE_RATIO,
    SKILL_TIERS, resolve_provider,
)

def test_provider_presets_have_required_keys():
    for name, preset in PROVIDER_PRESETS.items():
        assert "base_url" in preset
        assert "env_var" in preset

def test_abacus_preset():
    p = PROVIDER_PRESETS["abacus"]
    assert "abacus" in p["base_url"].lower() or "abacus" in p["env_var"].lower()

def test_resolve_provider_with_known_provider():
    base_url, env_var = resolve_provider("abacus")
    assert base_url == PROVIDER_PRESETS["abacus"]["base_url"]
    assert env_var == PROVIDER_PRESETS["abacus"]["env_var"]

def test_resolve_provider_with_base_url_override():
    base_url, env_var = resolve_provider("abacus", base_url_override="https://custom.api/v1")
    assert base_url == "https://custom.api/v1"

def test_resolve_provider_local():
    base_url, env_var = resolve_provider("local")
    assert "localhost" in base_url
    assert env_var is None

def test_resolve_provider_none_requires_base_url():
    base_url, env_var = resolve_provider(None, base_url_override="https://example.com/v1")
    assert base_url == "https://example.com/v1"

def test_constants():
    assert CHARS_PER_TOKEN == 4
    assert DEFAULT_TEMPERATURE == 0.7
    assert DEFAULT_MAX_TOKENS == 16384
    assert DEFAULT_PORT == 7860
    assert CONTEXT_RESERVE_RATIO == 0.75

def test_skill_tiers():
    assert "core" in SKILL_TIERS
    assert "gm" in SKILL_TIERS
    assert "full" in SKILL_TIERS
    assert set(SKILL_TIERS["core"]).issubset(set(SKILL_TIERS["gm"]))
    assert set(SKILL_TIERS["gm"]).issubset(set(SKILL_TIERS["full"]))
    assert "SKILL.md" in SKILL_TIERS["core"]
