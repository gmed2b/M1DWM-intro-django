from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Player, Inventory
from .forms import PlayerForm, ItemForm

# Create your views here.


def players(request):
    players = Player.objects.all()
    context = {"players": players}
    return render(request, "players.html", context)


def add_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            player_name = form.cleaned_data.get("player_name")
            player_level = form.cleaned_data.get("player_level")

            if Player.objects.filter(player_name=player_name).exists():
                form.add_error("player_name", "Player with this name already exists")
                return render(request, "add_player.html", {"form": form})

            if player_level < 0:
                form.add_error("player_level", "Player level cannot be negative")
                return render(request, "add_player.html", {"form": form})

            player = Player.objects.create(
                player_name=player_name, player_level=player_level
            )
            player.save()

            messages.success(request, "Player added successfully")

            return redirect("players")
        else:
            form.add_error(None, "Invalid form data")
            return render(request, "add_player.html", {"form": form})
    else:
        form = PlayerForm()
        context = {"form": form}
        return render(request, "add_player.html", context)


def view_player(request, player_id):
    try:
        player = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
        messages.error(request, "Player not found")
        return redirect("players")

    try:
        player_inventory = Inventory.objects.filter(player=player).all()
    except Inventory.DoesNotExist:
        player_inventory = None

    form = PlayerForm(
        data={"player_name": player.player_name, "player_level": player.player_level}
    )
    context = {"form": form, "player": player, "player_inventory": player_inventory}
    return render(request, "view_player.html", context)


def edit_player(request, player_id):
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)
    else:
        form = PlayerForm(request.POST)
        if form.is_valid():
            player_name = form.cleaned_data.get("player_name")
            player_level = form.cleaned_data.get("player_level")

            try:
                player = Player.objects.get(id=player_id)
                player.player_name = player_name
                player.player_level = player_level
                player.save()
            except Player.DoesNotExist:
                messages.error(request, "Player not found")
                return redirect("players")

            messages.success(request, "Player updated successfully")

            return redirect("view_player", player_id=player_id)
        else:
            form.add_error(None, "Invalid form data")
            return render(request, "edit_player.html", {"form": form})


def delete_player(request, player_id):
    try:
        player = Player.objects.get(id=player_id)
        player.delete()
        messages.success(request, "Player deleted successfully")
    except Player.DoesNotExist:
        messages.error(request, "Player not found")

    return redirect("players")


def add_item(request, player_id):
    try:
        player = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
        messages.error(request, "Player not found")
        return redirect("players")

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data.get("item_name")
            item_quantity = form.cleaned_data.get("item_quantity")

            if item_quantity < 0:
                form.add_error("item_quantity", "Item quantity cannot be negative")
                return render(
                    request, "add_item.html", {"form": form, "player": player}
                )

            Inventory.objects.create(
                player=player, item_name=item_name, item_quantity=item_quantity
            )
            messages.success(request, "Item added successfully")
            return redirect("view_player", player_id=player_id)
        else:
            form.add_error(None, "Invalid form data")
    else:
        form = ItemForm()

    context = {"form": form, "player": player}
    return render(request, "add_item.html", context)


def view_item(request, player_id, item_id):
    try:
        player = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
        messages.error(request, "Player not found")
        return redirect("players")

    try:
        item = Inventory.objects.get(id=item_id, player=player)
    except Inventory.DoesNotExist:
        messages.error(request, "Item not found")
        return redirect("view_player", player_id=player_id)

    form = ItemForm(
        data={"item_name": item.item_name, "item_quantity": item.item_quantity}
    )
    context = {"form": form, "player": player, "item": item}
    return render(request, "view_item.html", context)


def edit_item(request, player_id, item_id):
    try:
        player = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
        messages.error(request, "Player not found")
        return redirect("players")

    try:
        item = Inventory.objects.get(id=item_id, player=player)
    except Inventory.DoesNotExist:
        messages.error(request, "Item not found")
        return redirect("view_player", player_id=player_id)

    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)
    else:
        form = ItemForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data.get("item_name")
            item_quantity = form.cleaned_data.get("item_quantity")

            if item_quantity < 0:
                form.add_error("item_quantity", "Item quantity cannot be negative")
                return render(
                    request, "edit_item.html", {"form": form, "player": player}
                )

            item.item_name = item_name
            item.item_quantity = item_quantity
            item.save()

            messages.success(request, "Item updated successfully")
            return redirect("view_player", player_id=player_id)
        else:
            form.add_error(None, "Invalid form data")
            return render(
                request,
                "edit_item.html",
                {"form": form, "player": player, "item": item},
            )


def delete_item(request, player_id, item_id):
    try:
        player = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
        messages.error(request, "Player not found")
        return redirect("players")

    try:
        item = Inventory.objects.get(id=item_id, player=player)
        item.delete()
        messages.success(request, "Item deleted successfully")
    except Inventory.DoesNotExist:
        messages.error(request, "Item not found")

    return redirect("view_player", player_id=player_id)
