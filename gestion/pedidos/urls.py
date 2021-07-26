from django.urls import path
from pedidos import views
from pedidos.views import cursos, docentes, listado_docentes, eliminardocente, editardocente, listado_cursos
urlpatterns = [
    path('', views.docentes, name="docentes"),
    path('/cursos/', views.cursos, name="cursos"),
    path('/listado_docentes', views.listado_docentes, name="listado_docentes"),
    path('editardocente/<int:id>/', views.editardocente, name='editardocente'),
    path('eliminardocente/<int:id>/', views.eliminardocente, name='eliminardocente'),
    path('/listado_cursos', views.listado_cursos, name="listado_cursos"),
    path('editarcurso/<int:id>/', views.editarcurso, name='editarcurso'),
    path('eliminarcurso/<int:id>/', views.eliminarcurso, name='eliminarcurso'),
]