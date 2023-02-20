from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from users.serializers import *


""" Список пользователей. """
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

# """
# Список пользователей с пагинацией по 10 на странице.
# """
# class UserListView(ListView):
#     model = User
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#         # users = self.object_list.all()
#         self.object_list = self.object_list.order_by('username')
#         paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
#         page = request.GET.get('page')
#         obj = paginator.get_page(page)
#         response = {}
#         items_list = [
#             {'id': user.pk,
#              'first_name': user.first_name,
#              'last_name': user.last_name,
#              'username': user.username,
#              'password': user.password,
#              'role': user.role,
#              'age': user.age,
#              'locations': list(map(str, user.location.all())),
#              'total_ads': user.ads.filter(is_published=True).count()} for user in obj]
#         response['items'] = items_list
#         response['total'] = self.object_list.count()
#         response['num_pages'] = paginator.num_pages
#
#         return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


""" Информация об одном пользователе. """
class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

# """
# Вывод указанного пользователя.
# """
# class UserDetailView(DetailView):
#     # queryset = User.objects.all()
#     model = User
#
#     def get(self, request, *args, **kwargs):
#         user = self.get_object()
#
#         return JsonResponse({'id': user.pk,
#                              'first_name': user.first_name,
#                              'last_name': user.last_name,
#                              'username': user.username,
#                              'password': user.password,
#                              'role': user.role,
#                              'age': user.age,
#                              'locations': list(map(str, user.location.all())),
#                              'total_ads': user.ads.filter(is_published=True).count()
#                              }, safe=False, json_dumps_params={"ensure_ascii": False})


""" Создание пользователя. """
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

# """
# Создание пользователя.
# """
# @method_decorator(csrf_exempt, name='dispatch')
# class UserCreateView(CreateView):
#     model = User
#     fields = ['username']
#
#     def post(self, request, *args, **kwargs):
#         data = json.loads(request.body)
#         user = User.objects.create(
#             first_name=data['first_name'],
#             last_name=data['last_name'],
#             username=data['username'],
#             role=data['role'],
#             age=data['age'],
#         )
#
#         if 'locations' in data:
#             for loc_name in data['locations']:
#                 loc, _ = Location.objects.get_or_create(name=loc_name)
#                 user.location.add(loc)
#
#         return JsonResponse({'id': user.pk,
#                              'first_name': user.first_name,
#                              'last_name': user.last_name,
#                              'username': user.username,
#                              'role': user.role,
#                              'age': user.age,
#                              'locations': list(map(str, user.location.all())),
#                              }, safe=False, json_dumps_params={"ensure_ascii": False})

""" Обновление данных указанного пользователя. """
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

#
# """ Обновление данных указанного пользователя. """
# @method_decorator(csrf_exempt, name='dispatch')
# class UserUpdateView(UpdateView):
#     model = User
#     fields = ['username']
#
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#         data = json.loads(request.body)
#         if 'first_name' in data:
#             self.object.first_name = data['first_name']
#         if 'last_name' in data:
#             self.object.last_name = data['last_name']
#         if 'role' in data:
#             self.object.role = data['role']
#         if 'age' in data:
#             self.object.age = data['age']
#         if 'locations' in data:
#             for loc_name in data['locations']:
#                 loc, _ = Location.objects.get_or_create(name=loc_name)
#                 self.object.location.add(loc)
#         self.object.save()
#
#         return JsonResponse({'id': self.object.pk,
#                              'first_name': self.object.first_name,
#                              'last_name': self.object.last_name,
#                              'username': self.object.username,
#                              'password': self.object.password,
#                              'role': self.object.role,
#                              'age': self.object.age,
#                              'locations': list(map(str, self.object.location.all())),
#                              'total_ads': self.object.ads.filter(is_published=True).count()
#                              }, safe=False, json_dumps_params={"ensure_ascii": False})

"""Удаление указанного пользователя."""
class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersDestroySerializer

# """
# Удаление указанного пользователя.
# """
# @method_decorator(csrf_exempt, name='dispatch')
# class UserDeleteView(DeleteView):
#     model = User
#     success_url = "/"
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#         return JsonResponse({'status': 'ok'}, status=204)


"""
ViewSet для локаций.
"""
class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
