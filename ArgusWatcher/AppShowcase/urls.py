from django.urls import path
from .views import Tic_tac_toe, Connect_four


app_name = "AppShowcase"

urlpatterns = [
    # tic tac toe
    path(
        "showcase/tic-tac-toe/",
        Tic_tac_toe.as_view(),
        name="tic-tac-toe"
    ),
    # connect four
    path(
        "showcase/connect-four/",
        Connect_four.as_view(),
        name="connect-four"
    ),
]
