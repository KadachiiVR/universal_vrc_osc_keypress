import argparse
import re
import pyautogui
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer


g_prefix = ""


def keypress_handler(address, *args):
    global g_prefix
    print(f"Received: {address} -> {args}")
    suffix = address[len(g_prefix):]
    keys = re.split('\W+', suffix, flags=re.IGNORECASE)
    for key in keys:
        if not pyautogui.isValidKey(key):
            print(f"Error: {key} is not a valid keyname for pyautogui. Consult documentation for full valid key list.")

    state = bool(args[0])
    print(f"{'Pressing' if state else 'Releasing'} {'-'.join(keys)}")
    if state:
        for key in keys:
            pyautogui.keyDown(key)
    else:
        for key in keys:
            pyautogui.keyUp(key)


def fallback_handler(address, *args):
    pass


def main():
    global g_prefix
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1", help="IP address to listen for OSC messages from. Defaults to localhost.")
    parser.add_argument("--port", type=int, default=9001, help="Port to listen for OSC messages on. Defaults to 9001, the VRChat default.")
    parser.add_argument("--prefix", type=str, default="/avatar/parameters/key/", help="The OSC address prefix to look under for keypress commands. Defaults to /avatar/parameters/key/")
    args = parser.parse_args()
    g_prefix = args.prefix

    dispatcher = Dispatcher()
    dispatcher.map(args.prefix + "*", keypress_handler)
    dispatcher.set_default_handler(fallback_handler)

    server = BlockingOSCUDPServer((args.ip, args.port), dispatcher)
    print("Starting server!")
    server.serve_forever()


if __name__ == "__main__":
    main()