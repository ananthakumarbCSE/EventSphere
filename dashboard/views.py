from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.




#attendee pages








#organizer pages






#common pages

@login_required
def profile_page(request):
    pass



@login_required
def events_page(request):
    pass

@login_required
def event_page(request,event_id):
    pass

@login_required
def profile_view(request,username):
    pass
