from sample.models import Facility
from sample.models import User

facilitys = [
    ['施設', 'sisetu', '埼玉'],
    ['老人ホーム', 'rouzin', '東京'],
    ['介護', 'kaigo', '千葉'],
]

for facility in facilitys:
    facility_record = Facility(name=facility[0], password=facility[1], address=facility[2])
    facility_record.save()

users = [
    ['あひる', '宮原', '1'],
    ['ペンギン', '柏', '1'],
    ['アホウドリ', '安孫子', '2'],
    ['白鳥', '草加', '3'],
    ['スズメ', '春日部', '1'],
    ['フラミンゴ', '松戸', '2'],
]

for user in users:
    user_record = User(name=user[0], address=user[1], facility=user[2])
    user_record.save()