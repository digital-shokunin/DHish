import tempfile
from pathlib import Path
from campaign.journal import save_journal_entry, load_journal_entry, list_journal_entries, get_next_session_number

class TestJournal:
    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            save_journal_entry("# Session 1\nThe party met at a tavern.", 1, d)
            content = load_journal_entry(1, d)
            assert "tavern" in content

    def test_list_entries(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            save_journal_entry("Session 1", 1, d)
            save_journal_entry("Session 2", 2, d)
            entries = list_journal_entries(d)
            assert entries == [1, 2]

    def test_next_session_number_empty(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            assert get_next_session_number(Path(tmpdir)) == 1

    def test_next_session_number(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            save_journal_entry("S1", 1, d)
            save_journal_entry("S2", 2, d)
            assert get_next_session_number(d) == 3
