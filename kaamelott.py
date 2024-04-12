import irc.bot
import threading
import signal
import sys
import time
import random

# Dictionnaire des répliques pour chaque personnage
repliques = {
    "Arthur": [
        "C'est pas faux !",
        "Sire, j'ai l'intention de m'engager dans une explication dont même moi ne pourrai m'extraire.",
        "Vous avez tout à fait raison."
    ],
    "Perceval": [
        "On en a gros !",
        "C'est pas faux !",
        "Ah ben bravo, Moray !"
    ],
    "Karadoc": [
        "La poule, ça a pas de queue, c'est la poule !",
        "J'l'ai pas vu, j'l'ai pas senti !",
        "Moi, d'habitude, quand j'ai pas de dessert, je m'en vais, j'ai rien à foutre !"
    ],
    "Lancelot": [
        "Je ne suis pas sûûûr...",
        "Parfois il vaut mieux ne pas savoir, ça m'évite de raconter des conneries.",
        "Mais moi j'attends toujours le quatrième, c'est celui-là qui m'intéresse."
    ],
    "Merlin": [
        "Il y a du avoir méprise !",
        "La science n'explique pas tout !",
        "Ah, bah j'suis pas couché !"
    ],
    "Leodagan": [
        "Je suis le seigneur de Carmélide, et j'emmerde tout le monde !",
        "J'ai pas que ça à foutre, j'ai un château à gérer !",
        "Vous êtes tous des cons, j'ai envie de vous le dire !"
    ],
    "Dame Mevanwi": [
        "Je suis la femme de Karadoc, et j'ai mon mot à dire !",
        "Vous croyez que c'est facile de gérer un mari comme Karadoc ?",
        "Je suis la seule à pouvoir gérer les affaires de mon foyer."
    ],
    "Père Blaise": [
        "Je suis le prêtre de Kaamelott, et j'ai la foi !",
        "Je suis le seul à pouvoir gérer les affaires religieuses.",
        "Je suis le seul à pouvoir comprendre les codes de la morale."
    ],
    "Calogrenant": [
        "Je suis le chevalier le plus loyal de la Table Ronde.",
        "Je suis le seul à pouvoir gérer les affaires de mon royaume.",
        "Je suis le seul à pouvoir comprendre les codes de l'honneur."
    ],
    "Venec": [
        "Je suis le marchand le plus riche de Kaamelott, et j'ai tout ce que vous voulez !",
        "Je suis le seul à pouvoir gérer les affaires commerciales.",
        "Je suis le seul à pouvoir comprendre les codes de l'argent."
    ],
    "Dame Séli": [
        "Je suis la tante du roi Arthur, et j'ai une grande expérience des affaires de la cour.",
        "Je suis la seule à pouvoir gérer les affaires diplomatiques.",
        "Je suis la seule à pouvoir comprendre les codes de la politesse."
    ],
    "Yvain": [
        "Je suis le chevalier au lion, et j'ai un grand sens de l'honneur.",
        "Je suis le seul à pouvoir gérer les affaires de mon royaume.",
        "Je suis le seul à pouvoir comprendre les codes de la bravoure."
    ],
    "Gauvain": [
        "Je suis le chevalier aux deux épées, et j'ai un grand sens de la stratégie.",
        "Je suis le seul à pouvoir gérer les affaires de mon royaume.",
        "Je suis le seul à pouvoir comprendre les codes de la tactique."
    ],
    "Bohort": [
        "Je suis le chevalier au cerf, et j'ai un grand sens de la loyauté.",
        "Je suis le seul à pouvoir gérer les affaires de mon royaume.",
        "Je suis le seul à pouvoir comprendre les codes de l'amitié."
    ],
    "Guethenoc": [
        "Je suis le paysan le plus riche de Kaamelott, et j'ai un grand sens des affaires.",
        "Je suis le seul à pouvoir gérer les affaires agricoles.",
        "Je suis le seul à pouvoir comprendre les codes de la terre."
    ],
    "Elias": [
        "Je suis le moine le plus savant de Kaamelott, et j'ai un grand sens de la connaissance.",
        "Je suis le seul à pouvoir gérer les affaires intellectuelles.",
        "Je suis le seul à pouvoir comprendre les codes de la sagesse."
    ]
}

class KaamelottBot(irc.bot.SingleServerIRCBot):
    def __init__(self, nickname, channel, repliques):
        self.nickname = nickname
        self.channel = channel
        self.repliques = repliques
        irc.bot.SingleServerIRCBot.__init__(self, [("irc.extra-cool.fr", 6667)], nickname, nickname)

    def on_welcome(self, connection, event):
        print(f"{self.nickname} a rejoint le canal.")
        connection.join(self.channel)
        threading.Thread(target=self.send_random_message).start()  # Start the message sending thread

    def send_random_message(self):
        while True:
            try:
                reply = random.choice(self.repliques)
                response = f"<{self.nickname}> {reply}"
                self.connection.privmsg(self.channel, response)
                print(f"Message envoyé par {self.nickname}: {response}")
            except IndexError:
                print(f"Aucune réplique disponible pour {self.nickname}.")
            except Exception as e:
                print(f"Erreur lors de l'envoi du message pour {self.nickname}: {e}")
            time.sleep(60)  # Send a message every 60 seconds

# Create bots for each actor
bots = {
    "ArthurBot": KaamelottBot("Arthur", "#extra-cool", repliques["Arthur"]),
    "PercevalBot": KaamelottBot("Perceval", "#extra-cool", repliques["Perceval"]),
    "KaradocBot": KaamelottBot("Karadoc", "#extra-cool", repliques["Karadoc"]),
    "LancelotBot": KaamelottBot("Lancelot", "#extra-cool", repliques["Lancelot"]),
    "MerlinBot": KaamelottBot("Merlin", "#extra-cool", repliques["Merlin"]),
    "LeodaganBot": KaamelottBot("Leodagan", "#extra-cool", repliques["Leodagan"]),
    "DameMevanwiBot": KaamelottBot("Dame Mevanwi", "#extra-cool", repliques["Dame Mevanwi"]),
    "PereBlaiseBot": KaamelottBot("Père Blaise", "#extra-cool", repliques["Père Blaise"]),
    "CalogrenantBot": KaamelottBot("Calogrenant", "#extra-cool", repliques["Calogrenant"]),
    "VenecBot": KaamelottBot("Venec", "#extra-cool", repliques["Venec"]),
    "DameSeliBot": KaamelottBot("Dame Séli", "#extra-cool", repliques["Dame Séli"]),
    "YvainBot": KaamelottBot("Yvain", "#extra-cool", repliques["Yvain"]),
    "GauvainBot": KaamelottBot("Gauvain", "#extra-cool", repliques["Gauvain"]),
    "BohortBot": KaamelottBot("Bohort", "#extra-cool", repliques["Bohort"]),
    "GuethenocBot": KaamelottBot("Guethenoc", "#extra-cool", repliques["Guethenoc"]),
    "EliasBot": KaamelottBot("Elias", "#extra-cool", repliques["Elias"])
}

# Function to stop all bots properly
def stop_all_bots(signal, frame):
    for bot in bots.values():
        bot.disconnect("Shutdown")
    sys.exit(0)

if __name__ == "__main__":
    # Start all bots
    for bot in bots.values():
        threading.Thread(target=bot.start).start()

    # Capture the interrupt signal to stop the bots properly
    signal.signal(signal.SIGINT, stop_all_bots)
    signal.pause()
