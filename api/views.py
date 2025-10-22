from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def simple_api(request):
    """
    一个简单的API函数，用于前后端通信
    """
    if request.method == 'GET':
        # 返回简单的JSON响应
        data = {
            'message': 'Hello from backend!',
            'status': 'success'
        }
        return JsonResponse(data)
    
    elif request.method == 'POST':
        # 处理前端发送的数据
        try:
            # 获取前端发送的JSON数据
            received_data = json.loads(request.body.decode('utf-8'))
            name = received_data.get('name', 'Anonymous')
            
            # 返回处理后的数据
            response_data = {
                'message': f'Hello {name}! Your data was received.',
                'received': received_data,
                'status': 'success'
            }
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

def index(request):
    """
    渲染主页模板
    """
    return render(request, 'index.html')