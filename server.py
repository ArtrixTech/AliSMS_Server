import uuid
from mns.demo_sms_send import send_sms

from flask import Flask

app = Flask(__name__)


@app.route('/sendsms/<template>/<phone>/<content>')
def hello_world(template, phone, content):
    __business_id = uuid.uuid1()

    if not "SMS" in template:
        template = "SMS_44350355"

    params = "{\"name\":\"" + content + "\"}"
    res = send_sms(__business_id, phone, "Artrix雅智科技", template, params)

    print(res.decode())
    return res.decode()


if __name__ == '__main__':
    app.run(port=46338)
