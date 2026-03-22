from engine.agent import estimate_message_tokens, prune_messages

class TestEstimateMessageTokens:
    def test_single_message(self):
        msgs = [{"role": "user", "content": "hello world"}]
        assert estimate_message_tokens(msgs) > 0

    def test_includes_overhead(self):
        msgs = [{"role": "user", "content": ""}]
        assert estimate_message_tokens(msgs) == 10

    def test_multiple_messages(self):
        msgs = [
            {"role": "system", "content": "a" * 400},
            {"role": "user", "content": "b" * 40},
        ]
        assert estimate_message_tokens(msgs) == 130

class TestPruneMessages:
    def test_no_pruning_when_under_limit(self):
        msgs = [{"role": "system", "content": "sys"}, {"role": "user", "content": "hi"}]
        assert len(prune_messages(msgs, 10000)) == 2

    def test_preserves_system_message(self):
        sys_content = "x" * 4000
        msgs = [
            {"role": "system", "content": sys_content},
            {"role": "user", "content": "a" * 400},
            {"role": "assistant", "content": "b" * 400},
            {"role": "user", "content": "c" * 400},
        ]
        pruned = prune_messages(msgs, 1200)
        assert pruned[0]["role"] == "system"
        assert pruned[0]["content"] == sys_content

    def test_drops_oldest_first(self):
        msgs = [
            {"role": "system", "content": "sys"},
            {"role": "user", "content": "first"},
            {"role": "assistant", "content": "second"},
            {"role": "user", "content": "third"},
        ]
        pruned = prune_messages(msgs, 50)
        assert pruned[0]["content"] == "sys"
        if len(pruned) > 1:
            assert pruned[-1]["content"] == "third"
