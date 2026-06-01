"""
Base template class for GlassForge CLI.

Provides the abstract interface that all output templates must implement.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseTemplate(ABC):
    """Abstract base class for all output format templates.

    Each template subclass transforms the engine's configuration dictionary
    into framework-specific, ready-to-use code.
    """

    @abstractmethod
    def render(self, config: Dict[str, Any]) -> str:
        """Render the template with the given configuration.

        Args:
            config: Engine configuration dictionary containing all
                    CSS properties and derived values.

        Returns:
            Complete code string for the target framework.
        """
        pass

    @abstractmethod
    def file_extension(self) -> str:
        """Return the default file extension for this template type.

        Returns:
            File extension string including the dot (e.g., '.css').
        """
        pass

    @abstractmethod
    def description(self) -> str:
        """Return a human-readable description of this template type.

        Returns:
            Description string.
        """
        pass

    def default_filename(self) -> str:
        """Return a sensible default filename for the output.

        Returns:
            Default filename string with extension.
        """
        return f"liquid-glass{self.file_extension()}"
