from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("autocomplete_user/", views.autocomplete_user, name="autocomplete_user"),
    path("assign_task/<int:task_id>/", views.AssignTaskView.as_view(), name="assign_task"),
    path("create_team/", views.create_team, name="create_team"),
    path("create_invite/", views.InviteView.as_view(), name="create_invite"),
    path("remove_member/<int:member_id>/", views.RemoveMemberView.as_view(), name="remove_member"),
    path('delete_team/<int:team_id>/', views.DeleteTeamView.as_view(), name='delete_team'),
    path("press_invite/", views.press_invite, name="press_invite"),
    path('log_in/', views.LogInView.as_view(), name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('password/', views.PasswordView.as_view(), name='password'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('task_create/', views.CreateTaskView.as_view(), name='task_create'),
    path('task_search/', views.task_search, name='task_search'),
    path('task_delete/<int:pk>/', views.DeleteTaskView.as_view(), name='task_delete'),
    path('task_edit/<int:pk>/', views.TaskEditView.as_view(), name = 'task_edit'),
    path('task/<int:pk>/', views.TaskView.as_view(), name='task'),
    path('lane_delete/<int:lane_id>/', views.DeleteLaneView.as_view(), name='lane_delete'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('notif_delete/<int:notif_id>/',views.notif_delete,name='notif_delete')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)