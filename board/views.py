from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Item
from django.urls import reverse_lazy
# Create your views here.




#-----------------------------제네릭 뷰------------------------------------------------
class ItemLV(ListView):
    model = Item
    # ListView는 기본적 세팅
    # - templates: 앱 이름/모델명(소문자)_list.html
    # - context: object_list로 기본적으로 설정되어 있음
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['name'] = 'Tiger'
        return context
    
class ItemDV(DetailView):
    model = Item
    # DetailView는 기본 세팅
    # - template: 앱이름/모델면(소문자)_detail.html

class ItemCV(CreateView):
    model = Item
    success_url = reverse_lazy('index')
    fields = ['title', 'content']

#-----------------------------제네릭 뷰------------------------------------------------

#-----------------------------함수형 뷰------------------------------------------------

def itemLV(request):
    # 모델에서 데이터들 가져오고
    object = Item.objects.all()
    name = 'Lion'
    # context에 담고
    context = {
        'object_list':object,
        'name': name
    }
    # templates에 결합해서
    # 페이지를 반환
    return render(request=request, template_name='board/item_list.html', context=context)

def itemDV(request):
    pass

#-----------------------------함수형 뷰------------------------------------------------



def test(request):
    return HttpResponse("요청 확인")

def test1(request, pk):
    
    return HttpResponse(f"Test 1 {pk}번 입니다.")