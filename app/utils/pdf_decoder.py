"""
Base64 PDF decoding helpers.
"""

from __future__ import annotations

import base64
import binascii

from app.utils.exceptions import InvalidBase64Exception


def decode_pdf_content(content_b64: str) -> bytes:
    """
    Decode a Base64 string into PDF bytes.

    Performs strict validation of Base64 encoding before decoding.
    This ensures only valid Base64 strings are processed.

    Args:
        content_b64: Base64-encoded PDF content as a string

    Returns:
        The decoded PDF content as bytes

    Raises:
        ValueError: If the content is not valid Base64, with descriptive message
    """
    try:
        return base64.b64decode(content_b64, validate=True)
    except binascii.Error as exc:
        raise ValueError(
            "The content field must be valid Base64-encoded PDF data."
        ) from exc