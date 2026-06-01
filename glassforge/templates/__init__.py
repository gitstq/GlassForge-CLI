"""
Template package for GlassForge CLI.
"""

from .base import BaseTemplate
from .css import CSSTemplate
from .react import ReactTemplate
from .vue import VueTemplate
from .svelte import SvelteTemplate
from .html import HTMLTemplate

__all__ = [
    "BaseTemplate",
    "CSSTemplate",
    "ReactTemplate",
    "VueTemplate",
    "SvelteTemplate",
    "HTMLTemplate",
]

# Registry mapping output types to template classes
TEMPLATE_REGISTRY = {
    "css": CSSTemplate,
    "react": ReactTemplate,
    "vue": VueTemplate,
    "svelte": SvelteTemplate,
    "html": HTMLTemplate,
}


def get_template(output_type: str) -> BaseTemplate:
    """Get a template instance by output type name.

    Args:
        output_type: One of 'css', 'react', 'vue', 'svelte', 'html'.

    Returns:
        Template instance.

    Raises:
        ValueError: If the output type is not supported.
    """
    output_type = output_type.lower()
    if output_type not in TEMPLATE_REGISTRY:
        available = ", ".join(sorted(TEMPLATE_REGISTRY.keys()))
        raise ValueError(
            f"Unsupported output type '{output_type}'. Supported: {available}"
        )
    return TEMPLATE_REGISTRY[output_type]()
