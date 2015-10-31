from django.shortcuts import render

from core.acquire import WikiWrapper, Reader
from core.analyze import PhoneNumber


# Create your views here.
def search(request):
    phrase = request.GET.get('s', None)
    if phrase:
        adj = list()
        context = dict()
        ent_type = request.GET.get('t')
        ent_analyzer = WikiWrapper.search(phrase, int(ent_type))
        for res in ent_analyzer.pos_normalized['adjectives']:
            adj.append(res[0])
        context['adjectives'] = adj
        return render(request, 'search_form.tpl', context=context)
    else:
        return render(request, 'search_form.tpl')


def phone_number(request):
    context = None
    url = request.POST.get('url')

    if url:
        if not url.startswith('http'):
            url = 'http://{0}'.format(url)
        reader = Reader(url)
        numbers = PhoneNumber.extract_numbers(reader.data)

        if numbers:
            context = dict(numbers=numbers)

    return render(request, 'phone_search.tpl', context=context)

