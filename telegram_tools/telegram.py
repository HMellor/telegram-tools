import logging
from telethon import TelegramClient

logger = logging.getLogger(__name__)
required_configs = {"api_id", "api_hash", "token", "chat_id"}


class Bot:
    def __init__(self, config_path, name="bot"):
        self.name = name
        config_dict = self.__load_config(config_path)
        assert set(config_dict.keys()) == required_configs
        self.api_id = config_dict["api_id"]
        self.api_hash = config_dict["api_hash"]
        self.token = config_dict["token"]
        self.chat_id = config_dict["chat_id"]

    def __load_config(self, config_path):
        # get your api_id, api_hash, token
        # from telegram as described above
        config_dict = {}
        with open(config_path, "r") as config:
            for line in config:
                (key, val) = line.split("=")
                try:
                    val = float(val)
                    if val.is_integer():
                        val = int(val)
                except ValueError:
                    val = val.strip()
                config_dict[key] = val
        return config_dict

    def __start_client(self):
        client = TelegramClient(self.name, self.api_id, self.api_hash)
        client.start(bot_token=self.token)
        return client

    def send_message(self, message):
        client = self.__start_client()

        async def send_msg():
            try:
                # sending message using telegram client
                await client.send_message(self.chat_id, message, parse_mode="md")
            except Exception as e:
                # there may be many error coming in while like peer
                # error, wwrong access_hash, flood_error, etc
                print(e)

            # disconnecting the telegram session
            await client.disconnect()

        with client:
            client.loop.run_until_complete(send_msg())
