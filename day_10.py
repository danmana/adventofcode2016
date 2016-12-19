from util import maybe_download
import re


def apply_instruction(bots, outputs, s):
    give_re = re.compile(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)')
    value_re = re.compile(r'value (\d+) goes to bot (\d+)')

    m = value_re.match(s)
    if m is not None:
        val, bot_id = [int(x) for x in m.groups()]
        if bot_id not in bots:
            bot = Bot(bot_id)
            bots[bot_id] = bot
        else:
            bot = bots[bot_id]

        bot.feed(val)
    else:
        m = give_re.match(s)
        bot_id, low_type, low_id, high_type, high_id = m.groups()

        bot_id = int(bot_id)
        low_id = int(low_id)
        high_id = int(high_id)

        bot = get_or_create(bots, outputs, 'bot', bot_id)
        bot.low = get_or_create(bots, outputs, low_type, low_id)
        bot.high = get_or_create(bots, outputs, high_type, high_id)
        if len(bot.values) == 2:
            bot.feed_forward()



def get_or_create(bots, outputs, type, id):
    if type == 'bot':
        if id in bots:
            return bots[id]
        else:
            bot = Bot(id)
            bots[id] = bot
            return bot
    else:
        if id in outputs:
            return outputs[id]
        else:
            out = Output(id)
            outputs[id] = out
            return out





class Bot:
    def __init__(self, id: int):
        self.id = id
        self.values = []
        self.low = None
        self.high = None

    def feed(self, val: int):
        self.values.append(val)
        self.feed_forward()

    def feed_forward(self):
        if len(self.values) == 2 and self.low and self.high:
            self.values.sort()
            a, b = self.values
            if a == 17 and b == 61:
                print('part1:', self.id)

            self.low.feed(a)
            self.high.feed(b)
            self.values = []



class Output:
    def __init__(self, id):
        self.id = id
        self.values = []

    def feed(self, val: int):
        self.values.append(val)


def part1And2():
    bots = {}
    outputs = {}
    with maybe_download(10) as file:
        for s in file:
            s = s.strip()
            apply_instruction(bots, outputs, s)

        n = 1
        for out_id in [0,1,2]:
            for x in outputs[out_id].values:
                n *= x
        print('part2', n)




part1And2()