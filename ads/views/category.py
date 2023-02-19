# import json
# from django.http import JsonResponse
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from rest_framework.viewsets import ModelViewSet

from ads.models import Category
from ads.serializers.serializers_cat import CategorySerializer


"""
ViewSet для категорий.
"""
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#
# """
# Список категорий с пагинацией по 10 на странице.
# """
# class CategoryListView(ListView):
#     model = Category
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#         categories = self.object_list.all()
#         response = []
#         for category in categories:
#             response.append({
#                 'id': category.pk,
#                 'name': category.name,
#             })
#         return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})
#
#
# """
# Вывод указанной категории.
# """
# class CategoryDetailView(DetailView):
#     model = Category
#
#     def get(self, request, *args, **kwargs):
#         cat = self.get_object()
#         return JsonResponse({
#             'id': cat.pk,
#             'name': cat.name
#         }, safe=False)
#
#
# """
# Создание категории.
# """
# @method_decorator(csrf_exempt, name='dispatch')
# class CategoryCreateView(CreateView):
#     model = Category
#     fields = ['name']
#
#     def post(self, request, *args, **kwargs):
#         data = json.loads(request.body)
#         category = Category.objects.create(name=data['name'])
#         return JsonResponse({
#             'id': category.pk,
#             'name': category.name,
#         }, safe=False, json_dumps_params={"ensure_ascii": False})
#
#
# """
# Обновление указанной категории.
# """
# @method_decorator(csrf_exempt, name='dispatch')
# class CategoryUpdateView(UpdateView):
#     model = Category
#     fields = ['name']
#
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#         data = json.loads(request.body)
#         if 'name' in data:
#             self.object.name = data['name']
#         self.object.save()
#         return JsonResponse({
#             'id': self.object.pk,
#             'name': self.object.name,
#         }, safe=False, json_dumps_params={"ensure_ascii": False})
#
#
# """
# Удаление указанной категории.
# """
# @method_decorator(csrf_exempt, name='dispatch')
# class CategoryDeleteView(DeleteView):
#     model = Category
#     success_url = "/"
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#         return JsonResponse({'status': 'ok'}, status=204)
