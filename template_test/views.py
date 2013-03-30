from django.shortcuts import render_to_response
from django.http import HttpResponse
from certs.models import Cert


def test(request):
    certs = {"Cisco": ["CCENT", "CCNA", "CCNP", "CCIE"], "Microsoft":"", "VMware":"", "EC-Council":""}
    foo = 'hello world'
    return render_to_response('my_template.html', {
        'foo': foo,
        'certs': certs,
    })


def search_form(request):
    return render_to_response('search-form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        certs = Cert.objects.filter(name__icontains=q)
        return render_to_response('search-results.html',
            {'certs':certs, 'query':q})
    else:
        return HttpResponse("Please submit a search term")


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
