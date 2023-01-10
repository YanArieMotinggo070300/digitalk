# main.py
import cs_bot
from cs_bot import StartupConfig
from cs_bot.adapters import sop_bot

config = {
    "adapter": {"app_id": "ODgwOTA5NjgwMTQ1", "app_secret": "yuO4EitVC0SLsPK_WMIPrM2_5Q_h2zIb", "signing_secret": "lpvIJGn7S4VoHHX35s6UcNdNpUFFLB0u"}
}
cs_bot.init(StartupConfig.parse_obj(config))
cs_bot.register_adapter(sop_bot.Adapter)
cs_bot.load_plugin("plugins.echo")

if __name__ == '__main__':
    cs_bot.run(host="127.0.0.1", port=3000)