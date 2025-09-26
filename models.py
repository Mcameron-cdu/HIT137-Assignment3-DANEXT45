# models.py
# Contains BaseModel and subclasses for Hugging Face models

from transformers import pipeline


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
class TextGenerator(BaseModel):
    def __init__(self):
        super().__init__("distilgpt2", "text-generation")

    def run(self, input_data):
        result = self._pipeline(input_data, max_length=50, num_return_sequences=1)
        return result[0]["generated_text"]


# Image captioning model
class ImageCaptioner(BaseModel):
    def __init__(self):
        super().__init__("nlpconnect/vit-gpt2-image-captioning", "image-to-text")

    def run(self, input_data):
        result = self._pipeline(images=input_data)
        return result[0]["generated_text"]
