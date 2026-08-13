"""Baseline test: the scaffolded package imports correctly."""

import safe_medical_ai
from safe_medical_ai import config, llm, logging_setup, models, trace
from safe_medical_ai.api import main as api_main
from safe_medical_ai.llm.base import LLMAdapter
from safe_medical_ai.models.output_contract import (
    GeneratedResponsePlaceholder,
    NavigationContextPlaceholder,
    RuntimeEvidencePackagePlaceholder,
    ValidationOutcome,
)


def test_package_has_version():
    assert safe_medical_ai.__version__ == "0.1.0"


def test_submodules_importable():
    assert config is not None
    assert logging_setup is not None
    assert trace is not None
    assert models is not None
    assert llm is not None
    assert api_main is not None


def test_placeholder_models_are_instantiable():
    assert NavigationContextPlaceholder()
    assert RuntimeEvidencePackagePlaceholder()
    assert GeneratedResponsePlaceholder()


def test_validation_outcome_vocabulary():
    assert {o.value for o in ValidationOutcome} == {"PASS", "FAIL", "SAFE_FALLBACK"}


def test_llm_adapter_is_abstract():
    import pytest

    with pytest.raises(TypeError):
        LLMAdapter()  # abstract; must not be directly instantiable
