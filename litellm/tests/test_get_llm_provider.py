import os
import sys
import traceback

from dotenv import load_dotenv

load_dotenv()
import io
import os

sys.path.insert(
    0, os.path.abspath("../..")
)  # Adds the parent directory to the system path
import pytest

import litellm


def test_get_llm_provider():
    _, response, _, _ = litellm.get_llm_provider(model="anthropic.claude-v2:1")

    assert response == "bedrock"


# test_get_llm_provider()


def test_get_llm_provider_catch_all():
    _, response, _, _ = litellm.get_llm_provider(model="*")
    assert response == "openai"


def test_get_llm_provider_gpt_instruct():
    _, response, _, _ = litellm.get_llm_provider(model="gpt-3.5-turbo-instruct-0914")

    assert response == "text-completion-openai"


def test_get_llm_provider_mistral_custom_api_base():
    model, custom_llm_provider, dynamic_api_key, api_base = litellm.get_llm_provider(
        model="mistral/mistral-large-fr",
        api_base="https://mistral-large-fr-ishaan.francecentral.inference.ai.azure.com/v1",
    )
    assert custom_llm_provider == "mistral"
    assert model == "mistral-large-fr"
    assert (
        api_base
        == "https://mistral-large-fr-ishaan.francecentral.inference.ai.azure.com/v1"
    )
