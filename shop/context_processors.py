from .models import Category
def categories(request):
    cats = Category.objects.all().order_by("-id")
    # accounts = Account.objects.all()
    # telegram=instagram=phone=None
    # if Account.objects.filter(name=Account.TELEGRAM).exists():
    #     telegram = Account.objects.filter(name=Account.TELEGRAM).first().link
    # if Account.objects.filter(name=Account.PHONE_NUMBER).exists():
    #     phone = Account.objects.filter(name=Account.PHONE_NUMBER).first().link
    # if Account.objects.filter(name=Account.INSTAGRAM).exists():
    #     instagram = Account.objects.filter(name=Account.INSTAGRAM).first().link
    
    context = {
        "cats":cats,
    }
    return context