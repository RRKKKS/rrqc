from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 5826669564
bot_user = "gewgwe_bot"
api_id = 10823881
api_hash = "339886e2109eb67203ce12022b32e035"
session = "BAB5R-wPy4XrHuu6ljaI3VnlniZpsjRJA3g_wQMCOiOQb8Tg2N0WWoH0YCt_pRl1mGk1hMjXM-wNGYf4Br3gbmW-zJ4_urg0iBwqledv5DP4-8OXKeZNfET1_z-Z-behL0ycGm-HON8knAMYuX_0dnaZE0meK-qEiOKxNsCxLlgLwBTiPlzV9fJ7haXKdw9SEIDfP61_n4jRJ8roiq3IEEUOp0mJxy-hQoTe_qKSeU7Z2BHv7K2u9fmq48VerO9efKh4pmAPsID3HW7MgTqIV4BflI80DvYDNc7wjoS5_dn3pxn43zenJxw2ro5jTi3SM_uW9FfdwPTbb1lJIiD8DswsAAAAAT6f8toA"
token = "6400650393:AAE8gy30s612WAMp6lQ_F3t1inbpYAcwxLQ"
sudo_command = [5826669564, 5912085775]
pm = "5826669564"
mention = "5826669564"
plugins = dict(root="plugins")
app = Client("user:gewgwe_bot",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("gewgwe_bot",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
