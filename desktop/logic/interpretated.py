import requests


def interpretated(result, value):
    att = list(set(result))
    att.sort()
    answer = "Вы столкнулись со следующими опасностями: "

    reply = requests.get('http://localhost:23432/attack/')
    attacks = reply.json()
    print(attacks)
    attack_titles = [attack['type'] for attack in attacks]

    if value == 1:
        if len(att) > 1:
            if att[0] == 0:
                # Добавляем к строке элемент списка
                for i in range(1, len(att)):
                    answer += attack_titles[att[i]]
                    if i != len(att) - 1:
                        answer += ', '
            else:
                for i in range(0, len(att)):
                    answer += attack_titles[att[i]]
                    answer += ', '
        else:
            if att[0] == 0:
                answer = "Ваш трафик безопасен. Поздравляем!"

            else:
                answer = f"Вы столкнулись со следующей опасностью: {attack_titles[att[0]]}"
    else:
        if len(att) > 1:
            answer = "Ваш трафик содержит вредоносные элементы"
        else:
            if att[0] == 0:
                answer = "Ваш трафик безопасен. Поздравляем!"
            else:
                answer = "Ваш трафик содержит вредоносные элементы"
    return (answer)


