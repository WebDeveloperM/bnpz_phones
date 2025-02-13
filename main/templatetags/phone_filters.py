from django import template
import re

register = template.Library()

@register.filter
def clean_phone(value):
    """Telefon raqamdan faqat raqamlarni olib qoladi"""
    if value:
        return re.sub(r'[^\d]', '', value)
    return value  # Agar qiymat bo'sh bo'lsa, uni qaytaradi
