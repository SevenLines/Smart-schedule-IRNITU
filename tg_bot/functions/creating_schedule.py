from datetime import datetime, timedelta
import pytz
import locale

import platform

TZ_IRKUTSK = pytz.timezone('Asia/Irkutsk')
locale_name = ('ru_RU.UTF-8' if platform.system() == 'Linux' else 'ru_RU')
locale.setlocale(locale.LC_TIME, locale_name)

def full_schedule_in_str(schedule: list, week: str) -> list:
    schedule_str = []
    for one_day in schedule:
        day = one_day['day'].upper()
        lessons = one_day['lessons']

        lessons_str = '-------------------------------------------\n'
        for lesson in lessons:
            name = lesson['name']
            time = lesson['time']
            lesson_week = lesson['week']

            # смотрим только на пары из нужной недели
            if lesson_week != week and lesson_week != 'all':
                continue

            if name == 'свободно':
                lessons_str += f'<b>{time}</b>\n' \
                               f'{name}'

            else:
                aud = lesson['aud']
                if aud:
                    aud = f'Аудитория: {aud}\n'
                time = lesson['time']
                info = lesson['info'].replace(",", "")
                prep = lesson['prep']

                lessons_str += f'<b>{time}</b>\n' \
                               f'{aud}' \
                               f'{name}\n' \
                               f'{info} {prep}'
            lessons_str += '\n-------------------------------------------\n'

        schedule_str.append(f'\n<b>{day}</b>\n'
                            f'{lessons_str}')

    return schedule_str


def get_one_day_schedule_in_str(schedule: list, week: str) -> str:
    day_now = datetime.now(TZ_IRKUTSK).strftime('%A')
    for one_day in schedule:
        day = one_day['day']
        if day.lower() == day_now.lower():
            lessons = one_day['lessons']

            lessons_str = '-------------------------------------------\n'
            for lesson in lessons:
                name = lesson['name']
                time = lesson['time']
                lesson_week = lesson['week']

                # смотрим только на пары из нужной недели
                if lesson_week != week and lesson_week != 'all':
                    continue

                if name == 'свободно':
                    lessons_str += f'<b>{time}</b>\n' \
                                   f'{name}'

                else:
                    aud = lesson['aud']
                    if aud:
                        aud = f'Аудитория: {aud}\n'
                    time = lesson['time']
                    info = lesson['info'].replace(",", "")
                    prep = lesson['prep']

                    lessons_str += f'<b>{time}</b>\n' \
                                   f'{aud}' \
                                   f'{name}\n' \
                                   f'{info} {prep}'
                lessons_str += '\n-------------------------------------------\n'

            return f'\n<b>{day}</b>\n{lessons_str}'

def get_next_day_schedule_in_str(schedule: list, week: str) -> str:
    day_tomorrow = (datetime.now(TZ_IRKUTSK) + timedelta(days=1)).strftime('%A')
    for one_day in schedule:
        day = one_day['day']
        if day.lower() == day_tomorrow.lower():
            lessons = one_day['lessons']

            lessons_str = '-------------------------------------------\n'
            for lesson in lessons:
                name = lesson['name']
                time = lesson['time']
                lesson_week = lesson['week']

                # смотрим только на пары из нужной недели
                if lesson_week != week and lesson_week != 'all':
                    continue

                if name == 'свободно':
                    lessons_str += f'<b>{time}</b>\n' \
                                   f'{name}'

                else:
                    aud = lesson['aud']
                    if aud:
                        aud = f'Аудитория: {aud}\n'
                    time = lesson['time']
                    info = lesson['info'].replace(",", "")
                    prep = lesson['prep']

                    lessons_str += f'<b>{time}</b>\n' \
                                   f'{aud}' \
                                   f'{name}\n' \
                                   f'{info} {prep}'
                lessons_str += '\n-------------------------------------------\n'

            return f'\n<b>{day}</b>\n{lessons_str}'
