# ==========================================================
# MODULE: app.users
# ==========================================================
#
# Este módulo contém funções relacionadas a usuários.
#
# Ele demonstra que um módulo pode possuir várias funções,
# enquanto o package pode escolher quais delas serão
# disponibilizadas diretamente através de __init__.py.
#
# ==========================================================


def create_user(name: str) -> str:
    """Create a user."""
    return f"User created: {name}"


def delete_user(name: str) -> str:
    """Delete a user."""
    return f"User deleted: {name}"