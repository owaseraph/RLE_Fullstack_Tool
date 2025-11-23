from django.shortcuts import get_object_or_404
import json
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from .models import RLEHistory

@login_required
def save_history(request):
    if request.method == 'POST':
        try:
            # 1. Decode the JSON data coming from React
            data = json.loads(request.body)
            
            # 2. Save it to the database
            RLEHistory.objects.create(
                user=request.user,
                input_text=data.get('input_text'),
                output_text=data.get('output_text'),
                action_type=data.get('action_type'),
                ratio=data.get('ratio')
            )
            
            return JsonResponse({'status': 'success', 'message': 'History saved!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)

@login_required
def get_history(request):
    # 1. Get the last 10 entries for THIS user, newest first
    history_items = RLEHistory.objects.filter(user=request.user).order_by('-created_at')[:10]
    
    # 2. Convert database objects to JSON list
    data = []
    for item in history_items:
        data.append({
            'id': item.id,
            'action': item.action_type,
            'input': item.input_text[:30] + '...' if len(item.input_text) > 30 else item.input_text,
            'ratio': item.ratio,
            'date': item.created_at.strftime("%Y-%m-%d %H:%M")
        })
        
    return JsonResponse({'history': data})


@login_required
def delete_history_item(request, item_id):
    if request.method == 'POST':
        try:
            item = get_object_or_404(RLEHistory, id=item_id, user=request.user)
            item.delete()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
            
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)