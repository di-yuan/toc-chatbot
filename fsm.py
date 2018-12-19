from transitions.extensions import GraphMachine
from utils import send_text_message
from utils import send_image_url
import search
import search2

year = ["2016", "2017", "2018"]
mylist = []
addname = []

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_hello(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'hi'
        return False

    def is_going_to_wrong(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() not in year and text.lower() != "hi" and text.lower() != "list"
        return False

    def is_going_to_search(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() in year
        return False

    def is_going_to_list(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == "list"
        return False

    def is_going_to_comment(self, event):
        if event.get("message"):
            text = event['message']['text']
            return int(text) > 0 and int(text) <= len(search.name)
        return False

    def is_going_to_addYN(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == "y" or text.lower() == "n"
        return False

    def on_enter_hello(self, event):
        print("I'm entering hello")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "hi, choose 2016-2018 for korea drama ;)")
        self.go_back()

    def on_enter_wrong(self, event):
        print("I'm entering wrong")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Searching error... please choose 2016-2018 again ><")
        self.go_back()

    def on_enter_search(self, event):
        print("I'm entering search")

        sender_id = event['sender']['id']
        text = event['message']['text']
        send_text_message(sender_id, "You choose %s, wait a minute please <3" % text)
        search.search_drama(text)

        temp = ''
        for i in range(len(search.name)):
            temp += str(i+1) + '. ' + search.name[i] + '\n'
        send_text_message(sender_id, "%s" % temp)
        send_text_message(sender_id, "You can choose 1-%d to see comment and picture of drama ;)" % len(search.name))

    def on_enter_list(self, event):
        print("I'm entering list")

        sender_id = event['sender']['id']
        if len(mylist) == 0:
            send_text_message(sender_id, "List is empty, add some ! <3")
            send_text_message(sender_id, "Choose 2016-2018 to find ;)")
        else:
            temp = "Your list <3 \n"
            for i in range(len(mylist)):
                temp += str(i+1) + '. ' +mylist[i] + '\n'
            send_text_message(sender_id, "%s" % temp)
            send_text_message(sender_id, "Choose 2016-2018 to add more ! ;)")

        self.go_back()

    def on_enter_comment(self, event):
        print("I'm entering comment")

        sender_id = event['sender']['id']
        text = event['message']['text']
        send_text_message(sender_id, "You choose %s, wait a minute please <3" % search.name[int(text)-1])
        send_text_message(sender_id, "%s" % search.comment[int(text)-1])
        search2.search_pic(search.name[int(text)-1])
        send_image_url(sender_id, "%s" % search2.pic[len(search2.pic)-1])
        send_text_message(sender_id, "Do you want to add %s to your list ? (Y or N) ;)" % search.name[int(text)-1])
        addname.clear()
        addname.append(search.name[int(text)-1])

    def on_enter_addYN(self, event):
        sender_id = event['sender']['id']
        text = event['message']['text']
        if text.lower() == "y":
            mylist.append(addname[len(addname)-1])
            send_text_message(sender_id, "Add completely <3")
            send_text_message(sender_id, "Continue choosing drama or check your list by typing LIST ;)")
        else:
            send_text_message(sender_id, "Continue choosing drama to find the drama you like ;)")

