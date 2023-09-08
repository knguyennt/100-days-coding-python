import random

number_of_comparasion = 2

youtube_channel = [
    {
        'id': 1,
        'name': 'YN Vault',
        'subscribers': 22,
    },
    {
        'id': 2,
        'name': 'MrBeast',
        'subscribers': 181,
    },
    {
        'id': 3,
        'name': 'CN',
        'subscribers': 24,
    },
    {
        'id': 4,
        'name': 'Black Pink',
        'subscribers': 91,
    },
]

def get_comparasions_channels():
    random.shuffle(youtube_channel)

    channels = []
    for channel in range(0,number_of_comparasion):
        channels.append(youtube_channel[channel])

    return channels

def generate_questions(channels):
    question = ''
    for index, channel in enumerate(channels):
        question += f"{channel.get('name')}"

        if index == number_of_comparasion - 1:
            break

        question += ' vs '
    return question

def remove_channels():
    try:
        for i in range(number_of_comparasion):
            youtube_channel.pop(i)
    except:
        return


if __name__ == '__main__':
    while len(youtube_channel) >= 2:
        channels = get_comparasions_channels()
        question = generate_questions(channels)

        print(question)
        print('Which would have more subscribers (A) or (B)')
        answer = input()

        solution = 'A' if channels[0].get('subscribers') > channels[1].get('subscribers') else 'B'

        if answer == solution:
            print('You are correct')
            remove_channels()

        else:
            print('You lose')

    print('Out of question')
    
    
