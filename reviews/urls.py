from django.urls import path

from reviews.views import (
    GameReviewPageView,
    GameReviewsThanksView,
    GameReviewsDeleteView,
    GameReviewsDetailView,
    GameReviewsUpdateView,
    get_game_reviews,
    MyReviewsView,
    ReviewsPageView,
)

app_name = "reviews"
urlpatterns = [
    path("game-review/create/", GameReviewPageView.as_view(), name="create"),
    path("game-reviews/thanks/", GameReviewsThanksView.as_view(), name="thanks"),
    path("game-reviews/<slug>/update/", GameReviewsUpdateView.as_view(), name="update"),
    path("game-reviews/<slug>/delete/", GameReviewsDeleteView.as_view(), name="delete"),
    path(
        "game-reviews/<slug>/",
        GameReviewsDetailView.as_view(),
        name="details",
    ),
    path("get-game-reviews/", get_game_reviews, name="get-game-reviews"),
    path("my-reviews/", MyReviewsView.as_view(), name="my-reviews"),
    path("", ReviewsPageView.as_view(), name="reviews"),
]