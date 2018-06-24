from django.conf.urls import url

from polls.views import index

from polls.name import name

from polls.lista import lista


urlpatterns = [
    url(r'', index, name='index'),
]

urlpatterns = [
   url(r'', name, name='name'),
]

urlpatterns = [
    url(r'', lista, name='lista'),
]