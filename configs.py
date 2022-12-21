# (c) @AbirHasan2005

import os
import heroku3


class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = int(os.environ.get("API_ID", "1627545"))
    API_HASH = os.environ.get("API_HASH", "64e277a5e717aec5fecd067a34c35460")
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQAY1ZkAhkYX-cWDnDVCWzTyneN17d48G0aHwx5SA-2PWI-BDZeglaYkW2cgcrRIEUh1udvI6-3GOdJLm73TogVFHWaxgp8dEomm3R4bZpck2z4cNbzu6FNBI5Fdm81_XUnQ7yYiT6klKwunIkANBlbFd9k3lE3SC9hoQGXJRmhWB6RrzH0KvciVf_y-4pecvpMBlrK6gMNGYA3cFctyUd3Pcaiwuy8SDRgK6nTNU7Jtx9IpziCs_FQhTKsxcHuszt3_dvHT2r-E9YGtm9Uou23C5BdALeahIXV20-EV9ZcgzHZ5v_XP5HbfzzrHu9qe_HCypgdBi_KtHMUEZ7aA1S_m9bi5YwAAAAAvta3lAA")
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_FROM_CHAT_ID", "-1001723775557").split()))
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_TO_CHAT_ID", "-1001853735278").split()))
    # Filters for Forwards
    DEFAULT_FILTERS = "video document photo audio text gif forwarded poll sticker"
    FORWARD_FILTERS = list(set(x for x in os.environ.get("FORWARD_FILTERS", DEFAULT_FILTERS).split()))
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", "txt").split()))
    MINIMUM_FILE_SIZE = os.environ.get("MINIMUM_FILE_SIZE", None)
    BLOCK_FILES_WITHOUT_EXTENSIONS = bool(os.environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", False))
    # Forward as Copy. Value Should be True or False
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    # Sleep Time while Kang
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 10))
    # Heroku Management
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] if HEROKU_API_KEY and HEROKU_APP_NAME else None
    # Message Texts
    HELP_TEXT = """
This UserBot can forward messages from any Chat to any other Chat also you can kang all messages from one Chat to another Chat.

👨🏻‍💻 **Commands:**
• `!start` - Check UserBot Alive or Not.
• `!help` - Get this Message.
• `!kang` - Start All Messages Kanger.
• `!restart` - Restart Heroku App Dyno Workers.
• `!stop` - Stop Kanger & Restart Service.

©️ **Developer:** @AbirHasan2005
👥 **Support Group:** [【★ʟя★】](https://t.me/JoinOT)"""
