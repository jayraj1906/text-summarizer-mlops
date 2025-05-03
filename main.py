from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationPipeline

STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f"Stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Transformation Stage"
try:
    logger.info(f"Stage {STAGE_NAME} initiated")
    data_transformation_pipeline=DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e