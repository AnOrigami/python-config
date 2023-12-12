import yaml
from config import settings


class Obj:
    def __init__(
            self,
            listen,
            mongodb,
            redis
    ):
        self.listen = Listen(**listen)
        self.mongo = Mongo(**mongodb)
        self.redis = Redis(**redis)


class Listen:
    def __init__(self, port):
        self.port = port


class Mongo:
    def __init__(self, dsn, db):
        self.dsn = dsn
        self.db = db


class Redis:
    def __init__(self, dsn, db):
        self.dsn = dsn
        self.db = db


if __name__ == '__main__':
    # 打开 YAML 文件并读取内容
    with open('settings.yaml', 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    # 将 YAML 数据转换为 Python 对象
    obj_settings = Obj(**data)

    # 打印 Python 对象的属性
    print(type(obj_settings))
    # print(obj_settings.)
    print(type(settings))
