# ==========================================================
# PACKAGE INITIALIZATION
# ==========================================================
#
# __init__.py é executado quando o package "app" é carregado.
#
# Podemos utilizá-lo para definir uma interface pública
# conveniente para o package.
#
# A função create_user realmente está em:
#
#     app/users.py
#
# Mas ao importá-la aqui, permitimos:
#
#     import app
#     app.create_user(...)
#
# em vez de obrigar o usuário a conhecer:
#
#     app.users.create_user(...)
#
# ==========================================================


from .users import create_user


# Apenas create_user foi exposto diretamente pelo package.
#
# delete_user continua existindo em app.users, mas não foi
# colocado diretamente em app.