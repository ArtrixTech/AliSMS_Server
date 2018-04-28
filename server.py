
import json
import uuid
from mns.demo_sms_send import send_sms

def load_cfg():
    cfg=json.load("mns_cfg.json")
    return cfg["akid"],cfg["aksec"],cfg["end_point"]

accid,acckey,endpoint=load_cfg()
__business_id = uuid.uuid1()

params = "{\"name\":\"12345\"}"
print(send_sms(__business_id, "13632968596", "Artrix雅智科技", "SMS_44350355", params))
