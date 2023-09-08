from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView


class Tic_tac_toe(TemplateView):
    template_name = "AppShowcase/tic-tac-toe.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["title"] = "CSS Project: Tic Tac Toe"
        context["heading"] = "CSS Project: Tic Tac Toe"
        return context


class Connect_four(TemplateView):
    template_name = "AppShowcase/connect-four.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["title"] = "CSS + JS Project: Connect Four"
        context["heading"] = "CSS + JS Project: Connect Four"
        return context
