from django.shortcuts import render, get_object_or_404
from tlssite.models import Site
from django.contrib.auth.decorators import login_required, user_passes_test
from tlsscout.decorators import logged_in_or_anon_allowed
from django.core.urlresolvers import reverse, reverse_lazy
from taggit.models import Tag

@user_passes_test(logged_in_or_anon_allowed, login_url=reverse_lazy('account_login'))
def tag_details(request, tagslug):
    tag = get_object_or_404(Tag, slug=tagslug)
    sites = Site.objects.filter(tags__slug=tagslug)
    
    return render(request, 'tlssite/tag_sitelist.html', {
        'sites': sites,
        'tag': tag,
    })

@user_passes_test(logged_in_or_anon_allowed, login_url=reverse_lazy('account_login'))
def tag_list(request):
    # tags = Tag.objects.all()
    ### XXX why the hell is it so retarded to get all tags
    if Site.objects.all().count() == 0:
        tags = None
    else:
        tags = Site.objects.all()[0].tags.all()
        if Site.objects.all().count() > 1:
            for site in Site.objects.all():
                tags |= site.tags.all()
        ### remove duplicates
        tags = tags.distinct()
    return render(request, 'tlssite/tag_taglist.html', {
        'tags': tags
    })
