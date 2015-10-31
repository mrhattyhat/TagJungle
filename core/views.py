from django.shortcuts import render_to_response

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
        return render_to_response('search_form.tpl', context=context)
    else:
        return render_to_response('search_form.tpl')

def phone_number(request):
    context = None
    url = request.POST.get('url')

    if url:
        reader = Reader(url)
        context = PhoneNumber.extract_numbers(reader.data)

    if context:
        return render_to_response('phone_search.tpl', context=context)
    else:
        return render_to_response('phone_search.tpl')

