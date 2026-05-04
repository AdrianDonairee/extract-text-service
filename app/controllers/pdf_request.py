"""
Request model for PDF processing.
"""

from __future__ import annotations

import base64
import binascii

from pydantic import BaseModel, Field, field_validator


class PdfRequest(BaseModel):
    """
    Request body for PDF processing endpoint.

    Validates incoming PDF requests before processing to ensure
    both filename and content are present and content is valid Base64.
    """

    file_name: str = Field(min_length=1, description="Name of the PDF file")
    content: str = Field(min_length=1, description="PDF content encoded in Base64")

    @field_validator("content")
    @classmethod
    def validate_base64_content(cls, value: str) -> str:
        """
        Validate that content is strict Base64.

        Runs before model instantiation to reject invalid Base64 early,
        preventing wasted processing on invalid requests.

        Args:
            value: The content field value to validate

        Returns:
            The validated content string

        Raises:
            ValueError: If Base64 validation fails
        """
        try:
            base64.b64decode(value, validate=True)
        except binascii.Error as exc:
            raise ValueError("content must be a valid Base64 string") from exc

        return value