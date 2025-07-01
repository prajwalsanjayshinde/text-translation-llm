from transformers import pipeline

class Translator:
    def __init__(self):
        self.pipelines = {}
        self.supported_languages = [
            "ar", "bg", "zh", "cs", "da", "nl", "en", "et", "fi", "fr", "de", "el", "he", "hi", "hu",
            "id", "it", "ja", "ko", "lv", "lt", "mk", "no", "pl", "pt", "ro", "ru", "sk", "sl", "es",
            "sv", "tr", "uk", "vi"
        ]

    def load_model(self):
        pass  # Models are loaded on demand

    def translate_text(self, text, target_language):
        if not text:
            return ""
        if target_language not in self.supported_languages:
            raise ValueError(f"Unsupported language code: {target_language}")
        if target_language not in self.pipelines:
            model_name = f"Helsinki-NLP/opus-mt-en-{target_language}"
            try:
                self.pipelines[target_language] = pipeline("translation", model=model_name)
            except Exception:
                raise ValueError(f"Model for language '{target_language}' not available.")
        translator = self.pipelines[target_language]
        result = translator(text)
        return result[0]['translation_text']