from django.contrib import admin
from django.contrib.auth.decorators import login_required

# Register your models here.
@login_required
def java_page_view(request):
    return render(request,'testapp/javaexams.html')
