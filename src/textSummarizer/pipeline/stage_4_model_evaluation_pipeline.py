from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.model_evaluate import ModelEvaluation
class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def initiate_model_evaluation(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evalution=ModelEvaluation(config=model_evaluation_config)
        model_evalution.evaluate()

