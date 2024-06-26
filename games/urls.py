from django.urls import path

from games.views import (
    AnagramHuntView,
    LeaderBoardView,
    GameScoreDeleteView,
    GameScoreDetailView,
    MathFactsPlayView,
    MathFactsView,
    MyScoresView,
    record_score,
)

app_name = "games"
urlpatterns = [
    path("anagram-hunt/", AnagramHuntView.as_view(), name="anagram-hunt"),
    path("leaderboard/", LeaderBoardView.as_view(), name="leaderboard"),
    path("math-facts/", MathFactsView.as_view(), name="math-facts"),
    path("math-facts/play/", MathFactsPlayView.as_view(), name="math-facts-play"),
    path("my-scores/", MyScoresView.as_view(), name="my-scores"),
    path("record-score/", record_score, name="record-score"),
    path("game-scores/<slug>/delete", GameScoreDeleteView.as_view(), name="delete"),
    path("score-details/<slug>/", GameScoreDetailView.as_view(), name="score-details"),
]