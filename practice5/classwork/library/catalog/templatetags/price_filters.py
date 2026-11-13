from django import template

register = template.Library()

@register.filter
def format_price(value):
    """Форматирует число как цену: 1 250,50 ₽"""
    try:
        value = float(value)
    except (TypeError, ValueError):
        return value
    formatted = f"{value:,.2f}".replace(",", " ").replace(".", ",")
    return f"{formatted} ₽"
