from jinja2 import Environment, FileSystemLoader
import pandas as pd

if __name__ == '__main__':

    # Loading the DHCP record Template
    ENV = Environment(loader=FileSystemLoader('.'))
    tm = ENV.get_template("DHCP.j2")

    data = pd.read_csv("Data.csv")
    hostname = data['hostname']
    mac = data['mac']
    ip = data['ip']

    # Writing the DHCP configurations  into the STD output
    for i in range(len(mac)):
        print(tm.render(hostname=hostname[i], mac=mac[i], ip=ip[i]))
