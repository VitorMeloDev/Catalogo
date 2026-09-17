# ==========================================================
# MODULE: app.analytics.reports
# ==========================================================
#
# Estrutura:
#
#     app/
#     ├── users.py
#     │
#     └── analytics/
#         └── reports.py
#
# Este arquivo está dentro de:
#
#     app.analytics
#
# Para chegar até users.py, precisamos subir de analytics
# para app.
#
# Por isso utilizamos:
#
#     ..
#
# "from ..users" significa:
#
#     suba um nível no package e procure users.
#
# ==========================================================


from ..users import create_user


def generate_analytics_report() -> str:
    """Generate an analytics report using the users module."""
    user = create_user("Vitor")

    return f"Analytics report generated for: {user}"