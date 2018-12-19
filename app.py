from bottle import route, run, request, abort, static_file
from fsm import TocMachine

VERIFY_TOKEN = "123"

machine = TocMachine(
    states = ['user', 'hello', 'search', 'comment', 'addYN', 'wrong', 'list'],
    transitions = [
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'hello',
            'conditions': 'is_going_to_hello'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'wrong',
            'conditions': 'is_going_to_wrong'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'search',
            'conditions': 'is_going_to_search'
        },
        {
            'trigger': 'advance',
            'source': 'search',
            'dest': 'search',
            'conditions': 'is_going_to_search'
        },
        {
            'trigger': 'advance',
            'source': 'search',
            'dest': 'comment',
            'conditions': 'is_going_to_comment'
        },
        {
            'trigger': 'advance',
            'source': 'comment',
            'dest': 'addYN',
            'conditions': 'is_going_to_addYN'
        },
        {
            'trigger': 'advance',
            'source': 'addYN',
            'dest': 'list',
            'conditions': 'is_going_to_list'
        },
        {
            'trigger': 'advance',
            'source': 'addYN',
            'dest': 'search',
            'conditions': 'is_going_to_search'
        },
        {
            'trigger': 'advance',
            'source': 'addYN',
            'dest': 'comment',
            'conditions': 'is_going_to_comment'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'list',
            'conditions': 'is_going_to_list'
        },
        {
            'trigger': 'go_back',
            'source': [
                'hello',
                'wrong',
                'list'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)

