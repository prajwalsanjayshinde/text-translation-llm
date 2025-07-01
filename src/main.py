from transformers import pipeline

class Translator:
    def __init__(self):
        self.translator = None

    def load_model(self):
        # Default to English-to-Spanish; you can generalize this
        self.supported_languages = ['es', 'fr', 'de', 'it', 'pt']
        self.pipelines = {}

    def translate_text(self, text, target_language):
        if not text:
            return ""
        if target_language not in self.supported_languages:
            raise ValueError("Unsupported language code")
        if target_language not in self.pipelines:
            model_name = f"Helsinki-NLP/opus-mt-en-{target_language}"
            self.pipelines[target_language] = pipeline("translation", model=model_name)
        translator = self.pipelines[target_language]
        result = translator(text)
        return result[0]['translation_text']