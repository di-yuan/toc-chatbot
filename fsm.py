from transitions.extensions import GraphMachine
from utils import send_text_message
import search

year = ["2016", "2017", "2018"]

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state0(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'hi'
        return False

    def is_going_to_wrong(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() not in year and text.lower() != "hi"
        return False

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() in year
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return int(text) > 0 and int(text) <= len(search.name)
        return False

    def on_enter_state0(self, event):
        print("I'm entering state0")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "hi, choose 2016-2018 for korea drama ;)")
        self.go_back()

    def on_exit_state0(self):
        print('Leaving state0')

    def on_enter_wrong(self, event):
        print("I'm entering wrong")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Searching error... please choose 2016-2018 again ><")
        self.go_back()

    def on_exit_wrong(self):
        print('Leaving wrong')


    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        text = event['message']['text']
        send_text_message(sender_id, "You choose %s, wait a minute please <3" % text)
        search.search_drama(text)

        temp = ''
        for i in range(len(search.name)):
            temp += str(i+1) + '. ' + search.name[i] + '\n'
        send_text_message(sender_id, "%s" % temp)
        send_text_message(sender_id, "You can choose 1-%d to see comment of drama ;)" % len(search.name))

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        text = event['message']['text']
        send_text_message(sender_id, "You choose %s, wait a minute please <3" % search.name[int(text)-1])
        send_text_message(sender_id, "%s" % search.comment[int(text)-1])
        self.go_back()

