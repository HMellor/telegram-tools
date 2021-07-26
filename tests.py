import unittest
import telegram_tools
from pathlib import Path


class TestBot(unittest.TestCase):
    def setUp(self):
        config_path = Path(__file__).parent / "test.cfg"
        self.bot = telegram_tools.Bot(config_path)

    def test_config(self):
        self.assertEqual(self.bot.api_id, 1234)
        self.assertEqual(self.bot.api_hash, "1234ABCD")
        self.assertEqual(self.bot.token, "1234:ABCD")
        self.assertEqual(self.bot.chat_id, 1234)


if __name__ == "__main__":
    unittest.main(verbosity=2)
