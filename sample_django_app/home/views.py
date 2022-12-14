from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.apps import apps
from django.views.decorators.clickjacking import xframe_options_exempt
from shopify_app.decorators import known_shop_required, latest_access_scopes_required
from .forms import ImportForm


class HomeView(View):
    print("b-1")
    @xframe_options_exempt
    @known_shop_required
    @latest_access_scopes_required
    def get(self, request, *args, **kwargs):
        form = ImportForm()
        context = {
            "shop_origin": kwargs.get("shopify_domain"),
            "api_key": apps.get_app_config("shopify_app").SHOPIFY_API_KEY,
            "scope_changes_required": kwargs.get("scope_changes_required"),
            "form": form,
        }
        print(":b-1:",context)
        return render(request, "home/index.html", context)

class ApiView(View):
    print("b-2")
    @xframe_options_exempt
    @known_shop_required
    @latest_access_scopes_required
    def get(self, request, *args, **kwargs):
        context = {
            "shop_origin": kwargs.get("shopify_domain"),
            "api_key": apps.get_app_config("shopify_app").SHOPIFY_API_KEY,
            "scope_changes_required": kwargs.get("scope_changes_required"),
        }
        print(":b-2:",context)
        return render(request, "home/api_view.html", context)
