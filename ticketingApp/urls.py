from django.urls import re_path, path
from ticketingApp import views

urlpatterns = [
    re_path(r'^users/new$', views.user_new),
    re_path(r'^tickets/new$', views.tickets_new),
    re_path(r'^tickets/all$', views.tickets_list),
    re_path(r'^tickets/(?:status=(?P<status>\w+))?$', views.tickets_params),
    re_path(r'^tickets/markAsClosed$', views.tickets_close),
    re_path(r'^tickets/delete$', views.tickets_delete),

    # For testing purpose
    re_path(r'^users/all$', views.users_list),
    re_path(r'^tokens/all$', views.see_all_tokens),
    re_path(r'^ping/$', views.test_request),
]
