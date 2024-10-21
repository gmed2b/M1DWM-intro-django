from django.urls import path
from . import views

urlpatterns = [
    path("players/", views.players, name="players"),
    path("players/add", views.add_player, name="add_player"),
    path("players/<int:player_id>", views.view_player, name="view_player"),
    path("players/<int:player_id>/edit", views.edit_player, name="edit_player"),
    path("players/<int:player_id>/delete", views.delete_player, name="delete_player"),
    path("players/<int:player_id>/add_item/", views.add_item, name="add_item"),
    path(
        "players/<int:player_id>/view_item/<int:item_id>/",
        views.view_item,
        name="view_item",
    ),
    path(
        "players/<int:player_id>/edit_item/<int:item_id>/",
        views.edit_item,
        name="edit_item",
    ),
    path(
        "players/<int:player_id>/delete_item/<int:item_id>/",
        views.delete_item,
        name="delete_item",
    ),
]
