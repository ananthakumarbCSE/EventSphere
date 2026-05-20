from django.urls import path
from .views import profile_page,profile_view,events_page,event_page



urlpatterns = [
    
    
    #common routes
    
    #profile
    path("profile/",profile_page,name="profile_page"),
    path("profile/<str:username>/",profile_view,name="profile_view"),
    
    #events
    path("events/",events_page,name="events_page"),
    path("events/<int:event_id>/",event_page,name="event_page")
    
]
