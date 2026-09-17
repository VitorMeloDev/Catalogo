# ==========================================================
# CIRCULAR IMPORT EXAMPLE
# ==========================================================
#
# ATENÇÃO:
# Este módulo foi criado PROPOSITALMENTE com uma dependência
# circular.
#
# spellbook.py
#      |
#      v
# validator.py
#      |
#      v
# spellbook.py
#
# ==========================================================


from .validator import validate


def allowed_spells() -> str:
    """Return the spells allowed by the spellbook."""
    return "fire, water, earth"


def cast_spell(spell: str) -> str:
    """Try to cast a spell after validation."""
    return validate(spell)