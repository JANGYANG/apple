import boto3
from manitto.models import Apple

class Sms:
    def __init__(self):
        self.sender = boto3.client(
            "sns",
            aws_access_key_id="AKIAY7EBN7YWAXZZTZRQ",
            aws_secret_access_key="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",
            region_name="ap-northeast-1" # 도쿄
        )

    def send(self, name, phoneNum, manitto):
        # 주제나 구독자를 정하지 않으면 다음과 같이 간단하게 구현 가능
        self.sender.publish(
        PhoneNumber=phoneNum,
        Message= name + " 님은 " + manitto + " 에게 선물을 줍니다."
        )