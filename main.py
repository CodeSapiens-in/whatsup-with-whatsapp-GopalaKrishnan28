import re
from collections import Counter
from collections import defaultdict
def tokenize_line(line):
    
    words = re.findall(r'\b\w+\b', line.lower())
    return words


def get_sender(line):
    sender_match = re.search(r'^\[(.*?)\]', line)
    if sender_match:
        return sender_match.group(1).strip()
    return None

def extract_date(line):
    date_match = re.search(r'^\[(\d{2}/\d{2}/\d{2}),', line)
    if date_match:
        return date_match.group(1).strip()
    return None


with open("_chat.txt", 'r', encoding='utf-8') as fp:
    text = fp.readlines()


lines = len(text)
pollcount = 0

total_words = 0
word_counts = Counter()


sender_counts = Counter()


message_counts_by_date = Counter()

for eachline in text:
    
    if 'POLL' in eachline:
        pollcount += 1
    words = tokenize_line(eachline)
    total_words += len(words)
    word_counts.update(words)
    sender = get_sender(eachline)
    if sender:
        sender_counts[sender] += 1

    
    date = extract_date(eachline)
    if date:
        message_counts_by_date[date] += 1

print('Total Number of lines:', lines)
print('Total polls:', pollcount)
if lines > 0:
    average_words_per_line = total_words / lines
    print('Average words per line: {:.2f}'.format(average_words_per_line))
if message_counts_by_date:
    most_active_date = max(message_counts_by_date, key=message_counts_by_date.get)
    highest_message_count = message_counts_by_date[most_active_date]
    print('Date with the highest number of messages:')
    print(f'Date: {most_active_date}, Messages: {highest_message_count}')
else:
    print('No messages found in the chat.')
def get_sender(line):
    sender_match = re.search(r'\] (.+?):', line)
    if sender_match:
        return sender_match.group(1).strip()
    return None
sender_counts = Counter()

for line in text:
    sender = get_sender(line)
    if sender:
        sender_counts[sender] += 1
top_senders = sender_counts.most_common(3)
print('Top 3 persons who sent the most messages:')
for sender, count in top_senders:
    print(f'{sender}: {count} messages')
def extract_date1(line):
    date_match = re.search(r'^\[(\d{2}/\d{2}/\d{2}),', line)
    if date_match:
        return date_match.group(1).strip()
    return None




message_counts_by_date = Counter()

for eachline in text:
    date = extract_date1(eachline)
    if date:
        message_counts_by_date[date] += 1
print('Total number of messages for each day:')
for date, message_count in message_counts_by_date.items():
    print(f'Date: {date}, Messages: {message_count}')
def extract_date2(line):
    date_match = re.search(r'^\[(\d{2}/\d{2}/\d{2}),', line)
    if date_match:
        return date_match.group(1).strip()
    return None
def get_sender2(line):
    sender_match = re.search(r'] (.*?):', line)
    if sender_match:
        return sender_match.group(1).strip()
    return None
chatter_counts_by_date = {}

for eachline in text:
    date = extract_date2(eachline)
    if date:
        sender = get_sender2(eachline)
        if sender:
            if date in chatter_counts_by_date:
                chatter_counts_by_date[date].add(sender)
            else:
                chatter_counts_by_date[date] = {sender}
for date, chatters in chatter_counts_by_date.items():
    print(f'Date: {date}, Number of Chatters: {len(chatters)}')
def extract_date4(line):
    date_match = re.search(r'^\[(\d{2}/\d{2}/\d{2}),', line)
    if date_match:
        return date_match.group(1).strip()
    return None


def get_sender4(line):
    sender_match = re.search(r'] (.*?):', line)
    if sender_match:
        return sender_match.group(1).strip()
    return None
chatter_counts_by_date = {}

for eachline in text:
    # Extract the date from the line
    date = extract_date4(eachline)
    if date:
        sender = get_sender4(eachline)
        if sender:
            if date in chatter_counts_by_date:
                chatter_counts_by_date[date].add(sender)
            else:
                chatter_counts_by_date[date] = {sender}


chatter_days_count = Counter()

for date, chatters in chatter_counts_by_date.items():
    for chatter in chatters:
        chatter_days_count[chatter] += 1


chatters_at_least_10_days = [chatter for chatter, days in chatter_days_count.items() if days >= 10]

print(f'Number of chatters who have chatted on at least 10 different days: {len(chatters_at_least_10_days)}')
def extract_date5(line):
    date_match = re.search(r'^\[(\d{2}/\d{2}/\d{2}),', line)
    if date_match:
        return date_match.group(1).strip()
    return None

def get_sender5(line):
    sender_match = re.search(r'] (.*?):', line)
    if sender_match:
        return sender_match.group(1).strip()
    return None
chatter_counts_by_date = {}

for eachline in text:
    
    date = extract_date5(eachline)
    if date:
        sender = get_sender5(eachline)
        if sender:
            if date in chatter_counts_by_date:
                chatter_counts_by_date[date].add(sender)
            else:
                chatter_counts_by_date[date] = {sender}

total_days = len(chatter_counts_by_date)

threshold = int(0.9 * total_days)


chatter_days_count = Counter()

for date, chatters in chatter_counts_by_date.items():
    for chatter in chatters:
        chatter_days_count[chatter] += 1

chatters_almost_every_day = [chatter for chatter, days in chatter_days_count.items() if days >= threshold]


print(f'Number of chatters who chat almost every day ({threshold}+ days out of {total_days} days): {len(chatters_almost_every_day)}')
print(f'Chatters who chat almost every day ({threshold}+ days out of {total_days} days):')
for chatter in chatters_almost_every_day:
    print(chatter)
def extract_date6(line):
    date_match = re.search(r'^\[(\d{2}/\d{2}/\d{2}),', line)
    if date_match:
        return date_match.group(1).strip()
    return None
join_occurrences_by_date = Counter()

for eachline in text:
    
    date = extract_date6(eachline)
    if date:
        if "joined using this group's invite link" in eachline:
            join_occurrences_by_date[date] += 1
most_active_join_date = join_occurrences_by_date.most_common(1)
if most_active_join_date:
    date, count = most_active_join_date[0]
    print(f'Date with the most occurrences of "joined using the link": {date}, Occurrences: {count}')
else:
    print('No occurrences of "joined using the link" found in the chat.')

