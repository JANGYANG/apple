import boto3
from manitto.models import Apple

class Sms:
    def __init__(self):
        
        from manitto.aws_key import key_id, access_key

        self.sender = boto3.client(
            "sns",
            aws_access_key_id= key_id,
            aws_secret_access_key= access_key,
            region_name="ap-northeast-1" # 도쿄
        )

    def send(self, name, phoneNum, manitto):
        # 주제나 구독자를 정하지 않으면 다음과 같이 간단하게 구현 가능
        self.sender.publish(
        PhoneNumber=phoneNum,
        Message= name + " 님은 " + manitto + " 에게 선물을 줍니다."
        )