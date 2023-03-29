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
    facebook = "https://m.facebook.com/story.php?story_fbid=pfbid02nk2mYyBH9hzgUfUTWoZGmeWnFmCnPsKPcbQtbbwNZd6mUdFPaf1RxurD5PpkX613l&id=100063572289527&mibextid=qC1gEa"
    instagram = "https://www.instagram.com/zvukon.uz/"
    telegram = "https://t.me/zvukonuzb"
    phone = "+998909007666"
    adress = "Малика Базар А-блок 7магазин"
    context = {
        "cats": cats,
        "facebook": facebook,
        "instagram": instagram,
        "telegram": telegram,
        "phone" : phone,
        "adress": adress,
    }
    return context
