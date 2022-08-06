def input_numbers_to_int():
    input_string = input().split()
    return list(map(lambda x: int(x), input_string))


def input_numbers_to_float():
    input_string = input().split()
    return list(map(lambda x: float(x), input_string))


def her_favorite_number_1(numbers, preferred_percent):
    score = [0 for _ in range(len(numbers))]
    for i in range(10):
        for j in range(len(numbers)):
            if numbers[j] % 10 == i:
                score[j] = (10 - 10 / 9 * i) * preferred_percent
    return score


def her_favorite_number_2(numbers, preferred_percent):
    score = [0 for _ in range(len(numbers))]
    for i in range(51):
        for j in range(len(numbers)):
            if abs(50 - numbers[j]) == i:
                score[j] = (10 - 0.2 * i) * preferred_percent
    return score


def her_favorite_number_3(numbers, preferred_percent):
    score = [0 for _ in range(len(numbers))]
    for j in range(len(numbers)):
        if numbers[j] % 2:
            score[j] = 10 * preferred_percent
        else:
            score[j] = 0 * preferred_percent
    return score


def sum_scores(score1, score2, score3):
    sum_score = [0 for _ in range(len(score1))]
    for i in range(len(score1)):
        sum_score[i] = score1[i] + score2[i] + score3[i]
    return sum_score


def number_about_max_score(numbers, sum_score):
    max_score = 0
    count = 0
    for i in range(len(sum_score)):
        if max_score <= sum_score[i]:
            max_score = sum_score[i]
            count = i
    print("->")
    print(numbers[count])


def main():
    numbers = input_numbers_to_int()
    preferred_percents = input_numbers_to_float()
    score1 = her_favorite_number_1(numbers, preferred_percents[0])
    score2 = her_favorite_number_2(numbers, preferred_percents[1])
    score3 = her_favorite_number_3(numbers, preferred_percents[2])
    sum_score = sum_scores(score1, score2, score3)
    number_about_max_score(numbers, sum_score)


if __name__ == '__main__':
    main()
