import serial, bglib, time, datetime, json, urllib2
class NodeService(object):
    def __init__(self, port, one_meter_rssi, n):
        self.one_meter_rssi = one_meter_rssi
        self.n = n
        self.port_name = port
        self.baud_rate = 115200
        ble = bglib.BGLib()
        ble.packet_mode = False
        #setup our serial port
        ser = serial.Serial(port=self.port_name, baudrate=self.baud_rate, timeout=1)
        ser.flushInput()
        ser.flushOutput()

        #add our bluetooth events
        ble.on_timeout += self.timeout
        ble.ble_evt_gap_scan_response += self.ble_evt_gap_scan_response

         # disconnect if we are connected already
        ble.send_command(ser, ble.ble_cmd_connection_disconnect(0))
        ble.check_activity(ser, 1)

        # stop advertising if we are advertising already
        ble.send_command(ser, ble.ble_cmd_gap_set_mode(0, 0))
        ble.check_activity(ser, 1)

        # stop scanning if we are scanning already
        ble.send_command(ser, ble.ble_cmd_gap_end_procedure())
        ble.check_activity(ser, 1)

        # set scan parameters
        ble.send_command(ser, ble.ble_cmd_gap_set_scan_parameters(0x0400, 0x0400, 0))
        ble.check_activity(ser, 1)

        # start scanning now
        ble.send_command(ser, ble.ble_cmd_gap_discover(1))
        ble.check_activity(ser, 1)

        while (1):
            # check for all incoming data (no timeout, non-blocking)
            ble.check_activity(ser)

            # don't burden the CPU
            time.sleep(0.1)

    def ble_evt_gap_scan_response(self,sender,  args):
        t = datetime.datetime.now()
        disp_list = []
        # print args
        disp_list.append("%ld.%03ld" % (time.mktime(t.timetuple()), t.microsecond/1000))
        disp_list.append("%d" % args["rssi"])
        disp_list.append("%d" % args["packet_type"])
        disp_list.append("%s" % ''.join(['%02X' % b for b in args["sender"][::-1]]))
        disp_list.append("%d" % args["address_type"])
        disp_list.append("%d" % args["bond"])
        disp_list.append("%s" % ''.join(['%02X' % b for b in args["data"]]))
        # if(['%02X' % b for b in args["sender"][::-1]] == ['CC', 'FC', 'FB', '24', 'C0', '05']):
        # print ','.join(disp_list)
        self.calculate_and_post_distance("%ld.%03ld" % (time.mktime(t.timetuple()), t.microsecond/1000), ''.join(['%02X' % b for b in args["sender"][::-1]]),args["rssi"])

    def calculate_and_post_distance(self, milliseconds,sender, rssi):
        est_distance = 10**(-(rssi + self.one_meter_rssi)/(10*self.n))
        print milliseconds,sender,rssi,est_distance
        # print(est_distance)
        # data = json.dumps([
        # {
        #     "device_id":"C5E2F0FF1863",
        #     "rssi_data":-65,
        #     "distance": 25,
        #     "timestamp": 1387043362,
        #     "node_id":"node_1",
        #     "confidence":2,
        #     "location_x":0,
        #     "location_y":54
        # },
        # {
        #     "device_id":"CCFCFB24C005",
        #     "rssi_data":-64,
        #     "distance": 10,
        #     "timestamp": 1387043362,
        #     "node_id":"node_1",
        #     "confidence":3,
        #     "location_x":0,
        #     "location_y":54
        # }
        # ])
        data = json.dumps([
        {
            "device_id": sender,
            "rssi_data": rssi,
            "distance": int(est_distance * 1000),
            "timestamp":int(float(milliseconds)),
            "node_id": "node_2",
            "confidence": 0,
            "location_x":0,
            "location_y":0
        }
        ])
        url = 'http://localhost:8000/node_input/'
        req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
        f = urllib2.urlopen(req)
        response = f.read()
        f.close()

        

    def timeout(self, sender, args):
        # might want to try the following lines to reset, though it probably
        # wouldn't work at this point if it's already timed out:
        #ble.send_command(ser, ble.ble_cmd_system_reset(0))
        #ble.check_activity(ser, 1)
        print("BGAPI parser timed out. Make sure the BLE device is in a known/idle state.")

service = NodeService('/dev/tty.usbmodem1', 65, 1.5)

