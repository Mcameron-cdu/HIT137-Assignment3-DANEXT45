from transformers import pipeline   # Import the hugging face pipeline function

# template for all models
class BaseModel:
    def __init__(self, model_name, task): # takes the hugging face model name and the task
        self._model_name = model_name 
        self._task = task
        self._pipeline = None # stores the details

    def load(self):
        self._pipeline = pipeline(self._task, model=self._model_name) # Load the hugging face model

    def run(self, input_data):
        raise NotImplementedError("Subclasses must override this method") # this is a placeholder line for the models to override when run

    def get_info(self):
        return f"Model: {self._model_name}\nTask: {self._task}" # generates some information about the actual model


# text generation model
class TextGenerator(BaseModel):
    def __init__(self):
        super().__init__("distilgpt2", "text-generation") # Tells the constructor the model name and task
    def run(self, input_data):
        result = self._pipeline(input_data, max_length=50, num_return_sequences=1)
        return result[0]["generated_text"] # takes text input, generates new text and returns it


# image reading model
class ImageCaptioner(BaseModel):
    def __init__(self):
        super().__init__("nlpconnect/vit-gpt2-image-captioning", "image-to-text") # Tells the constructor the model name and task

    def run(self, input_data):
        result = self._pipeline(images=input_data)
        return result[0]["generated_text"] # takes image file path input, generates text and returns it
