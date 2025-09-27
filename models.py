# models.py
# Contains BaseModel and subclasses for Hugging Face models

from transformers import pipeline

# A decorator to make sure the models are loaded before the program is run
def ensure_loaded(func):
    def wrapper(self, *args, **kwargs):
        if self._pipeline is None:
            self.load()
        return func(self, *args, **kwargs)
    return wrapper

# A mixin class to log the use of the model in a text file
import datetime
class LoggerMixin:
    LOG_FILE = "model.log"

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}\n"
        with open(self.LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry)

# Base template for all models
class BaseModel:
    def __init__(self, model_name, task):
        self._model_name = model_name
        self._task = task
        self._pipeline = None

    def load(self):
        """Load the Hugging Face model into a pipeline."""
        self._pipeline = pipeline(self._task, model=self._model_name)

    def run(self, input_data):
        """Must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override this method")

    def get_info(self):
        """Return information about the model."""
        return f"Model: {self._model_name}\nTask: {self._task}"

# Text generation model
class TextGenerator(LoggerMixin, BaseModel):
    def __init__(self):
        super().__init__("distilgpt2", "text-generation")

    @ensure_loaded
    def run(self, input_data):
        self.log(f"Running TextGenerator with input: {input_data}")
        result = self._pipeline(input_data, max_length=50, num_return_sequences=1)
        return result[0]["generated_text"]


# Image captioning model
class ImageCaptioner(LoggerMixin, BaseModel):
    def __init__(self):
        super().__init__("nlpconnect/vit-gpt2-image-captioning", "image-to-text")

    @ensure_loaded
    def run(self, input_data):
        self.log(f"Running ImageCaptioner with image: {input_data}")
        result = self._pipeline(images=input_data)
        return result[0]["generated_text"]
