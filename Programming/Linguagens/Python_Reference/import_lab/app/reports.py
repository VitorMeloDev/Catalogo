# ==========================================================
# MODULE: app.reports
# ==========================================================
#
# Este módulo precisa utilizar create_user(), que pertence
# ao módulo users.py.
#
# Como reports.py e users.py estão dentro do mesmo package,
# podemos utilizar um import relativo:
#
#     from .users import create_user
#
# O "." significa:
#
#     "partindo do package atual"
#
# ==========================================================


from .users import create_user


def generate_report() -> str:
    """Generate a simple report using the users module."""
    user = create_user("Vitor")

    return f"Report generated for: {user}"