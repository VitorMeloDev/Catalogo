# ==========================================================
# CIRCULAR IMPORT EXAMPLE
# ==========================================================
#
# Este módulo também depende de spellbook.py.
#
# Isso cria:
#
#     spellbook
#          |
#          v
#     validator
#          |
#          v
#     spellbook
#
# ==========================================================


from .spellbook import allowed_spells


def validate(spell: str) -> str:
    """Validate a spell against the spellbook."""
    return f"{spell} checked against {allowed_spells()}"