# lesgo_utils.py oke

def hype_message(name="friend"):
    phrases = [
        "Let's GO! 🚀",
        "We got this! 💪",
        "Charge ahead, {}! 🔥".format(name),
        "Victory awaits! 🎯"
    ]
    for phrase in phrases:
        print(phrase)

if __name__ == "__main__":
    hype_message("Lesgo Dev")
