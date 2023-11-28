from django.contrib import admin
from .models import User, Team, Invite,Task

# Register your models here.
admin.site.register(Task)
"""These haven't been fully finished, but seem to work for what is needed so far"""

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Configuration of the adminstrative interface for users"""
    list_display = [
        "username", "first_name", "last_name", "email", "is_active"
    ]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Configuration of the adminstrative interface for users"""
    list_display = [
        "team_name", "get_members", "description"
    ]

    def get_members(self, team):
        return [user.username for user in team.get_team_members().all()]


@admin.register(Invite)
class InviteAdmin(admin.ModelAdmin):
    """Configuration of the adminstrative interface for invites"""
    list_display = [
        "get_invited_users", "get_team", "invite_message"
    ]

    def get_invited_users(self, invite):
        return [user.username for user in invite.invited_users.all()]
    
    
    def get_team(self, invite):
        return [team.team_name for team in invite.inviting_team.all()]