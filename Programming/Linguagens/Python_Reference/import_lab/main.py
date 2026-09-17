# ==========================================================
# IMPORT LAB
# ==========================================================
#
# Este arquivo demonstra diferentes formas de importar
# módulos, funções e packages.
#
# ==========================================================


# ----------------------------------------------------------
# 1. import module
# ----------------------------------------------------------
#
# Importamos o módulo inteiro.
#
# Depois do import, "tools" passa a ser um nome disponível
# neste arquivo.
#
# Para acessar algo dentro dele usamos:
#
#     tools.greet()
#     tools.add()
#
# ----------------------------------------------------------

import tools


print("=== 1. import module ===")
print(tools.greet("Vitor"))
print(tools.add(10, 20))


# ----------------------------------------------------------
# 2. from module import name
# ----------------------------------------------------------
#
# Aqui importamos diretamente uma função específica.
#
# "greet" passa a existir diretamente neste namespace.
#
# Por isso podemos escrever:
#
#     greet(...)
#
# em vez de:
#
#     tools.greet(...)
#
# ----------------------------------------------------------

from tools import greet


print("\n=== 2. from module import name ===")
print(greet("Vitor"))


# ----------------------------------------------------------
# 3. import package.module
# ----------------------------------------------------------
#
# "app" é um package.
# "users" é um módulo dentro desse package.
#
# Podemos acessar:
#
#     app.users.create_user()
#
# ----------------------------------------------------------

import app.users


print("\n=== 3. import package.module ===")
print(app.users.create_user("Vitor"))


# ----------------------------------------------------------
# 4. from package.module import name
# ----------------------------------------------------------
#
# Podemos importar diretamente uma função de um módulo
# que está dentro de um package.
#
# ----------------------------------------------------------

from app.users import delete_user


print("\n=== 4. from package.module import name ===")
print(delete_user("Vitor"))


# ----------------------------------------------------------
# 5. import package
# ----------------------------------------------------------
#
# O package "app" possui um __init__.py.
#
# Esse __init__.py define quais nomes queremos disponibilizar
# diretamente através de "app".
#
# Neste caso:
#
#     app.create_user()
#
# ----------------------------------------------------------

import app


print("\n=== 5. import package ===")
print(app.create_user("Vitor"))


# ----------------------------------------------------------
# 6. Módulo usando outro módulo
# ----------------------------------------------------------
#
# reports.py precisa de users.py.
#
# A dependência é:
#
#     reports.py
#          |
#          v
#       users.py
#
# ----------------------------------------------------------

from app.reports import generate_report


print("\n=== 6. Module importing another module ===")
print(generate_report())


# ----------------------------------------------------------
# 7. Package com subpackage
# ----------------------------------------------------------
#
# Agora temos:
#
#     app/
#       analytics/
#           reports.py
#
# Podemos acessar esse módulo usando seu caminho completo.
#
# ----------------------------------------------------------

from app.analytics.reports import generate_analytics_report


print("\n=== 7. Package + subpackage ===")
print(generate_analytics_report())