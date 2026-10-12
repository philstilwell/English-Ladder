"""Shared configuration for paid lesson-writing and editorial-review requests."""

MODEL_NAME = "gemini-3.1-pro-preview"
THINKING_LEVEL = "high"
MAX_OUTPUT_TOKENS = 65_536


def structured_generation_config(response_json_schema):
    """Keep drafting, targeted repairs, and final review on one request policy."""
    return {
        "response_mime_type": "application/json",
        "response_json_schema": response_json_schema,
        "max_output_tokens": MAX_OUTPUT_TOKENS,
        "thinking_config": {"thinking_level": THINKING_LEVEL},
    }
