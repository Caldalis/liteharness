"""Custom exception hierarchy for liteharness."""


class LiteHarnessError(Exception):
    """Base exception for all liteharness errors."""


class ConfigError(LiteHarnessError):
    """Raised when configuration is invalid or cannot be loaded."""


class LLMError(LiteHarnessError):
    """Raised when an LLM provider call fails after retries."""


class MCPError(LiteHarnessError):
    """Raised when an MCP server connection or call fails."""


class SkillError(LiteHarnessError):
    """Raised on skill discovery or parsing failures."""


class ToolError(LiteHarnessError):
    """Raised on tool registration or execution failures."""
