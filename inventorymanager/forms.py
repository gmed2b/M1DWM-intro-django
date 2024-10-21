from django import forms


class PlayerForm(forms.Form):
    player_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Player Name",
                "class": "px-5 py-3 rounded-md bg-martinique-950",
                "autofocus": "true",
            }
        )
    )
    player_level = forms.IntegerField(
        initial=0,
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Player Level",
                "class": "px-5 py-3 rounded-md bg-martinique-950",
            }
        ),
    )


class ItemForm(forms.Form):
    item_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Item Name",
                "class": "px-5 py-3 rounded-md bg-martinique-950",
                "autofocus": "true",
            }
        )
    )
    item_quantity = forms.IntegerField(
        initial=1,
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Item Quantity",
                "class": "px-5 py-3 rounded-md bg-martinique-950",
            }
        ),
    )
