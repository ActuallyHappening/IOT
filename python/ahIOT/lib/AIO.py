import Adafruit_IO as AIO

class Aio:
  client: AIO.Client
  schema: dict[str, str]
  
  def __init__(self, username: str, password: str, scheme: dict[str, str] = {
    "group": "brad",
    "data": "test_data",
    "status": "test_status",
    "control": "test_control",
  }):
    self.client = AIO.Client(username, password)
    self.schema = scheme
  
  @classmethod
  def send(cls, group: str, feed: str, *, data):
      fullName = group + "." + feed
      cls.client.send(fullName, data)
  
  @classmethod
  def receive(cls, group: str, feed: str):
      fullName = group + "." + feed
      return cls.client.receive(fullName)

  @classmethod
  def send_schema(cls, scheme_option, data):
    cls.client.send(cls.scheme.group, cls.schema.keys[scheme_option], data)
    
  @classmethod
  def receive_schema(cls, scheme_option):
    return cls.client.receive(cls.scheme.group, cls.schema.keys[scheme_option])

  def send_data(self, data):
      self.send_schema("data", data=data)
  
  def send_status(self, data):
    self.send("status", data=data)

  def receive_control(self):
      return self.receive_schema("control")