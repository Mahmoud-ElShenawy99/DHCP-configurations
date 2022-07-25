from jinja2 import Template
import random
import pandas as pd
from faker import Faker


# extending the functionality of Faker to fulfill my need
class MyFaker(Faker):
    def __init__(self):
        Faker.__init__(self)
        # Template for the IP address
        self.ip_tmp = Template("{{num1}}.{{num2}}.{{num3}}.{{num4}}")
        # Template for the mac address
        self.mac_tmp = Template("{{num1}}:{{num2}}:{{num3}}:{{num4}}:{{num5}}:{{num6}}")

    # A function that generates a random IP address in the format X.X.X.X
    def ip(self):
        return self.ip_tmp.render(num1=random.randrange(0, 255), num2=random.randrange(0, 255),
                                  num3=random.randrange(0, 255), num4=random.randrange(0, 255))

    # A function that generates a random MAC address in the format X.X.X.X.X.X
    def mac(self):
        return self.mac_tmp.render(num1=hex(random.randrange(0, 255))[2:], num2=hex(random.randrange(0, 255))[2:],
                                   num3=hex(random.randrange(0, 255))[2:], num4=hex(random.randrange(0, 255))[2:],
                                   num5=hex(random.randrange(0, 255))[2:], num6=hex(random.randrange(0, 255))[2:])


# Driver code to generate Fake Data
if __name__ == '__main__':
    F = MyFaker()
    ip = []
    mac = []
    hostname = []

    for i in range(1000):
        ip.append(F.ip())
        mac.append(F.mac())
        hostname.append(F.name())

    dict = {'hostname': hostname, 'mac': mac, 'ip': ip}
    df = pd.DataFrame(dict)
    df.to_csv('Data.csv', header=True, index=False)
    print("d")
