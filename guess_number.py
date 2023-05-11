from random import randint

from num_to_words import num_to_words


def create_number() -> str:
    number: str = ''
    while len(number) < 4:
        digit: str = str(randint(0, 9))
        if digit not in number:
            number += digit
    return number


def guess_number(number: str) -> int:
    counter_steps: int = 0
    counter_k: int = 0
    while counter_k != 4:
        new_number: str = input('Введите число: ')
        counter_steps += 1
        counter_k = 0
        counter_b: int = 0
        for i in range(len(new_number)):
            if not new_number[i].isdigit():
                guess_number(number)
            if new_number[i] == number[i]:
                counter_k += 1
            elif new_number[i] in number:
                counter_b += 1
        print(counter_steps, new_number, end=' ')
        print(f'{counter_k}K {counter_b}B')
    print('WIN!')
    return counter_steps


def main() -> None:
    record: int = 10**100000
    while True:
        number: str = create_number()
        count: int = guess_number(number=number)
        correct_count_word: str = num_to_words(count, ('шаг', 'шага', 'шагов'))
        print(f'Тебе понадобилось: {count} {correct_count_word}')
        record = count if count < record else record
        correct_record_word: str = num_to_words(
            record, ('шаг', 'шага', 'шагов'))
        print(f'Твой рекорд: {record} {correct_record_word}')
        if input('Сыграем ещё? (y/N) ') != 'y':
            break


if __name__ == '__main__':
    main()
