# Universal VRChat OSC Keypress Receiver
### The simplest way to press buttons without using any kind of overlay!

## Usage
Universal OSC Keypress watches for certain animator parameters to change and then tries to press and/or release keys that have the same name. For example, if you have on your avatar a parameter named `key/alt-f4`, whenever that parameter switches to `true`, this program will emulate a keypress down for `Alt-F4`, and when that parameter switches to `false`, this program will release those keys. Simple use cases include pressing Alt-F9, the default hotkey to toggle nVidia Shadowplay recording, or to use with a custom push-to-talk hotkey in discord.

To run it, you can just double-click the .exe, or use a command line (or make a shortcut) to specify launch options as detailed below:

```
$> universal_osc_keypress.exe --help
usage: universal_osc_keypress.py [-h] [--ip IP] [--port PORT]
                                 [--prefix PREFIX]

optional arguments:
  -h, --help       show this help message and exit
  --ip IP          IP address to listen for OSC messages from. Defaults to
                   localhost.
  --port PORT      Port to listen for OSC messages on. Defaults to 9001, the
                   VRChat default.
  --prefix PREFIX  The OSC address prefix to look under for keypress commands.
                   Defaults to /avatar/parameters/key/
```

## Avatar setup (simple)
Just add a parameter to your parameters object for the key you want to press (`key/alt-f9` for example), and then add a menu option to toggle it. That's it.

## Avatar setup (fancy)
Instead of using a menu to toggle it, use contacts and parameter drivers to create the exact control setup you want. For example, a contact zone on the side of your head that toggles your push-to-talk key. Still pretty easy. That's the point!

## Get in touch!
- Ask me about stuff in the helpdesk discord: https://discord.gg/9n77EvEg
- @ me on twitter: https://twitter.com/KadachiiVR
- More cool stuff on GitHub: https://github.com/KadachiiVR/knuckles_to_osc