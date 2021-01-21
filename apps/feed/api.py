import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import rot
@login_required
def api_add_rot(request):
    data = json.loads(request.body)
    body = data['body']

    rot_ = rot.objects.create(body=body,created_by=request.user)

    return JsonResponse({'success':True})