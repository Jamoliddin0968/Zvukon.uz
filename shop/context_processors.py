from .models import Category
from users.models import Account
def categories(request):
    cats = Category.objects.all().order_by("-name")
    accounts = Account.objects.all()
    telegram=instagram=phone=None
    if Account.objects.filter(name=Account.TELEGRAM).exists():
        telegram = Account.objects.filter(name=Account.TELEGRAM).first().link
    if Account.objects.filter(name=Account.PHONE_NUMBER).exists():
        phone = Account.objects.filter(name=Account.PHONE_NUMBER).first().link
    if Account.objects.filter(name=Account.INSTAGRAM).exists():
        instagram = Account.objects.filter(name=Account.INSTAGRAM).first().link
    context = {
        "cats":cats,
        "accounts":accounts,
        "telegram":telegram,
        "instagram":instagram,
        "phone":phone
    }
    return context