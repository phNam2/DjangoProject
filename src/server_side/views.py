from django.shortcuts import render

# Create your views here.
def server(request, *args, **kwargs):
	return render(request, "index.html", {})