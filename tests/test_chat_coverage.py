from chat import Chat


class DummyToolCall:
    def __init__(self):
        self.function = type("F", (), {
            "name": "calculate",
            "arguments": '{"expression": "2+2"}'
        })
        self.id = "test_id"


class DummyResponseTool:
    def __init__(self):
        self.choices = [
            type("Choice", (), {
                "message": type("Msg", (), {
                    "tool_calls": [DummyToolCall()],
                    "content": None
                })()
            })
        ]


class DummyResponseFinal:
    def __init__(self):
        self.choices = [
            type("Choice", (), {
                "message": type("Msg", (), {
                    "tool_calls": None,
                    "content": "4"
                })()
            })
        ]


def test_tool_call_branch(monkeypatch):
    chat = Chat()

    calls = [DummyResponseTool(), DummyResponseFinal()]

    def fake_create(*args, **kwargs):
        return calls.pop(0)

    monkeypatch.setattr(chat.client.chat.completions, "create", fake_create)

    response = chat.send_message("2+2", temperature=0.0)

    assert "4" in response