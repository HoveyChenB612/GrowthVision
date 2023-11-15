from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse


def index_main(request):
	"""主页"""

	return render(request, "index_main.html")
