from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from django.views import static
from home import urls as home_urls
from blog import urls as blog_urls
from accounts import urls as accounts_urls
from coffee import urls as coffee_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls
from search import urls as search_urls
from filters import urls as filter_urls
from orderhistory import urls as history_urls
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(home_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^coffee/', include(coffee_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^search/', include(search_urls)),
    url(r'^filter/', include(filter_urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^orderhistory/', include(history_urls)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
