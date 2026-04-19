from chat import Chat
from tools.compact import compact


def test_provider_models():
    assert "openai" in Chat(provider="openai").MODEL
    assert "anthropic" in Chat(provider="anthropic").MODEL
    assert "google" in Chat(provider="google").MODEL
    assert Chat(provider="groq").provider == "groq"

class DummyMessage:
    def __init__(self, role, content):
        self.role = role
        self.content = content


def test_compact_function_runs():
    messages = [
        {"role": "user", "content": "hello"},   # dict case
        DummyMessage("assistant", "hi")         # object case
    ]
    summary = compact(messages)
    assert isinstance(summary, str)
    assert len(summary) > 0


def test_compact_replaces_messages():
    chat = Chat()
    chat.messages = [
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": "hi"}
    ]

    summary = compact(chat.messages)
    chat.messages = [{"role": "system", "content": summary}]

    assert len(chat.messages) == 1