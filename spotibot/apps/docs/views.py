from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="spotibot",
        description=f"github repo: https://github.com/fedecalendino/spotibot",
        default_version="v1",
    ),
    public=True,
)
