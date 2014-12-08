from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'game.app.views.new_game', name='home'),
    url(r'^games/(?P<player_id>[0-9]+)$', 'game.app.views.game', name='game'),

    ### API ###
    url(r'^api/status$', 'game.app.views.get_current_state', name='status'),
    url(r'^api/update$', 'game.app.views.update', name='update'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

