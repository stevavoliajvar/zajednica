from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostCreateView2,
    PostUpdateView,
    PostDeleteView,
    # 	MngrMessageListView,
    # 	MsgDetailView,
    # 	MsgDeleteView,
    # 	CheckMessagesView,
    # 	MessageListView
)
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path("home/", views.home, name="app-home"),
    path("home_user/", PostListView.as_view(), name="app-home-user"),
    path("home_manager/", views.home_manager, name="app-home-manager"),
    path("", views.frontpage, name="app-frontpage"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path(
        "post/anketa/<int:anketa_id>/<str:anketa_title>",
        PostCreateView2.as_view(),
        name="post-create2",
    ),
    path("about/", views.about, name="app-about"),
    path("reciklaza_/", views.reciklaza, name="app-reciklaza"),
    path("reciklaza/cepovi", views.cepovi, name="reciklaza-cepovi"),
    path("tag/<slug:slug>", views.tagged, name="app-tagged"),
    path("telefoni/", views.telefoni, name="app-telefoni"),
    path("telefoni_p/", views.telefoni_p, name="app-telefoni-public"),
    path(
        "upravnik_postovi/<int:pk>",
        views.upravnik_posts, name="upravnik-posts"
        ),
    path("papirlist/", views.TempPapirList.as_view()),
    path("prijavljeni_cepovi/", views.TempCepoviList.as_view()),
    path("api/papir/<int:pk>", views.UlazPapirList.as_view()),
    path("base_layout", views.base_layout, name="base_layout"),
    path("gradelist/", views.GradesList.as_view()),
    path("p_mapa/", views.PapirMapa.as_view()),
    path("c_mapa/", views.CepoviMapa.as_view()),
    path("cep_total/<str:address>", views.CepTotal.as_view()),
    path("papir_prijava/", csrf_exempt(views.PapirPrijava.as_view())),
    path("cep_prijava/", csrf_exempt(views.CepPrijava.as_view())),
    path("cep_confirmation/", csrf_exempt(views.CepConfirmation.as_view())),
    path("cepovi_list/<str:address>", csrf_exempt(views.CepoviList.as_view())),
    path("api/", views.apiOverview),
    path("post/<int:pk>/like", csrf_exempt(views.post_like))
    # path(
    # 'manager_messages/', MngrMessageListView.as_view(), name="mngr-messages"
    # ),
    # path('messages/<int:pk>', MsgDetailView.as_view(), name="msg-detail"),
    # path(
    # 'messages/<int:pk>/delete', MsgDeleteView.as_view(), name="msg-delete"
    # ),
    # path(
    # 'check_messages/<str:pk>',
    # CheckMessagesView.as_view(),
    # name='check-messages'
    # ),
    # path('messages_list/', MessageListView.as_view(), name='message-list')
]
