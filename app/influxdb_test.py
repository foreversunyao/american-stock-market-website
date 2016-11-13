import argparse

from influxdb import InfluxDBClient


def main(host='localhost', port=8086):
    user = 'root'
    password = 'root'
    dbname = 'example'
    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west",
		"up":100,
		"down":50
            },
            "time": "2016-10-25T23:00:00Z",
            "fields": {
                "value": 0.64,
		"volume":100
            }
        }
    ]

    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'stock_frequent_data')
    client.write_points(json_body)
#    client = InfluxDBClient(host, port, user, password, dbname)
#
#    print("Create a retention policy")
#    client.create_retention_policy('awesome_policy', '3d', 3, default=True)
#
#    print("Write points: {0}".format(json_body))
#    client.write_points(json_body)
#


def parse_args():
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False, default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port)
