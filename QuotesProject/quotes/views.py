from django.shortcuts import render, redirect
from quotes.models import Quote
from random import randint
from quotes.forms import QuoteForm
from django.contrib import messages
from django.db.models import Sum

# Create your views here.
def index(request):
    totalWeight = Quote.objects.aggregate(total=Sum("weight"))["total"]
    if totalWeight:
        target = randint(0, totalWeight - 1)
        for curr in Quote.objects.iterator():
            target -= curr.weight
            if target < 0:
                quote = curr
                break
        quote.views += 1
        quote.save()
    else:
        quote = None
    return render(request, 'quotes/index.html', {'quote': quote})

def top(request):
    return render(request, "quotes/top.html", {'quotes': Quote.objects.order_by('-likes', 'dislikes', 'views')[:10]})

def add(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Цитата успешно добавлена!')
            return redirect('quotes:add')
        else:
            for field, errors in form.errors.items():
                field_name = form.fields[field].label if field in form.fields else field
                for error in errors:
                    messages.error(request, f"{field_name}: {error}")
    else:
        form = QuoteForm()
    
    return render(request, 'quotes/add.html', {'form': form})


def like(request, quoteId):
    try:
        quote = Quote.objects.get(id=quoteId)
        quote.likes += 1
        quote.save()
    except Quote.DoesNotExist:
        messages.error(request, 'Не удалось лайкнуть')
    return redirect('quotes:index')

def dislike(request, quoteId):
    try:
        quote = Quote.objects.get(id=quoteId)
        quote.dislikes += 1
        quote.save()
    except Quote.DoesNotExist:
        messages.error(request, 'Не удалось дизлайкнуть')
    return redirect('quotes:index')
