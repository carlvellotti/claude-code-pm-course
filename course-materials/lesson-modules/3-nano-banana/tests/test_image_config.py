import image_gen


def test_image_config_includes_image_size(monkeypatch):
    captured = {}

    # Fake ImageConfig to capture kwargs
    def fake_image_config(**kwargs):
        captured.update(kwargs)
        return "IMGCONF"

    monkeypatch.setattr(image_gen.types, "ImageConfig", fake_image_config)

    # Fake GenerateContentConfig to assert it receives our fake image_config
    def fake_generate_content_config(**kwargs):
        assert kwargs.get("response_modalities") == ['TEXT', 'IMAGE']
        assert kwargs.get("image_config") == "IMGCONF"
        return "GENCONF"

    monkeypatch.setattr(image_gen.types, "GenerateContentConfig", fake_generate_content_config)

    # Stub out network client, session loading/saving, and response
    class DummyResponse:
        parts = []

    class DummyChat:
        def send_message(self, content_parts):
            return DummyResponse()

    class DummyChats:
        def create(self, model, config, history=None):
            return DummyChat()

    class DummyClient:
        chats = DummyChats()

    monkeypatch.setattr(image_gen, "_get_client", lambda: DummyClient())
    monkeypatch.setattr(image_gen, "_load_session", lambda: {"history": [], "outputs": [], "turn": 0})
    monkeypatch.setattr(image_gen, "_save_session", lambda s: None)

    # Call generate with resolution="4K"
    result = image_gen.generate("test prompt", aspect_ratio="1:1", resolution="4K", model="gemini")

    # Ensure image_size was passed through
    assert captured.get("image_size") == "4K"
