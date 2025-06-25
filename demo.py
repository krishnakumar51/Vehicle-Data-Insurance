from src.pipline.training_pipeline import TrainPipeline
from dotenv import load_dotenv
load_dotenv()  # Automatically loads .env from current or parent dir

pipeline = TrainPipeline()
pipeline.run_pipeline()