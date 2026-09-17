# ==========================================================
# MODULE: tools
# ==========================================================
#
# Qualquer arquivo .py pode ser utilizado como um módulo.
#
# Este módulo será importado por main.py para demonstrar:
#     import tools
#     from tools import greet
#
# ==========================================================


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b