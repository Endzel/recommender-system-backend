from django.apps import AppConfig

class RecommenderConfig(AppConfig):

    name = 'recommender'

    def ready(self):
        import recommender.signals
