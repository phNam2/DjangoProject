from django.shortcuts import render

# Create your views here.
from .models import Manhattan
def table_view(request, *args, **kwargs):
	items = Manhattan.objects.all()
	context = {
        'items': items,
	}
	return render(request, "show_table.html", context)