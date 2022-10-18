import configparser
cfg = configparser.ConfigParser()
cfg.add_section("Telegram")
cfg.set("Telegram", "api_id", "Place your 'api_id' here.")
cfg.set("Telegram", "api_hash", "Place your 'api_hash' here.")
cfg.set("Telegram", "username", "Place your 'username' here.")
with open('config.ini', 'w') as my_cfg:
    cfg.write(my_cfg)