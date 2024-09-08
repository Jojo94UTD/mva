from django.urls import path
from .views import index_nav, avis, carte, remerciement, repertoire, ville_detail, contribuer
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index_nav, name="navigate-index"),
    path('repertoire/', repertoire, name='repertoire'),
    path('ville/<int:idVille>/', ville_detail, name='ville-detail'),
    path('avis/', avis, name='avis'),
    path('carte/', carte, name='carte'),
    path('remerciement/', remerciement, name='remerciement'),
    path('contribuer/', contribuer, name='contribuer'),

    # Racine pour index_nav
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
