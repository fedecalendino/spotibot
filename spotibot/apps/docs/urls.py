from django.urls import path

from . import views

urlpatterns = [
    path(
        route="swagger",
        view=views.schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        route="schema.json",
        view=views.schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
]
