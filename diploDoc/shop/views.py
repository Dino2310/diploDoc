from django.shortcuts import render
from .models import*

def index(request):
    ad = Marketing.objects.all()
    prod = Product.objects.all()[:4]

    content = {
        'prod' : prod,
        'ad' : ad
    }
    return render(request, 'shop/index.html', content)
=======
    return render(request, 'shop/index.html', content)
>>>>>>> b68cdf655362cc333c3045fa9cb7a0eb0bac9809
