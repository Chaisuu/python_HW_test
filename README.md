# Учебный проект по Python

## Описание:

Проект X - это приложение на Python для управления банковскими операциями, конвертацией фалют в RUB.
***
Функции:
***
get_mask_card_number - Функция которая возвращает маску карты
get_mask_account - Функция которая маскирует номер счета
filter_by_state - Фильтрует список словарей по значению ключа 'state'.
sort_by_date - Функция принимает на вход список словарей и возвращает новый список,отсортированыq по убыванию даты
get_mask_card_number - Функция которая возвращает маску карты
get_mask_account - Функция которая возвращает маску счета
get_date - функция которая проебразует дату.
get_read_json - фукнция которая возварщает список словарей в заданном пути
get_amount_transactions - функция которая возвращает сумму в рублях
get_amount_convert -  фнукция которая делает конвертацию по api из USD, EUR в RUB
*** 
Тесты
***
test.mask.py - тестирует функции get_mask_card_number и get_mask_account
test.widget - тестирует функции get_mask_card_number, get_mask_account  и get_date
test.processing - тестирует функции filter_by_state и sort_by_date
test.generator - тестирует функции filter_by_currency, card_number_generator и transaction_descriptions
test_get_read_json - тест фукнции  get_read_json
test_get_amount_transactions - тест фукнции get_amount_transactions
test_get_amount_convert - тест функции get_amount_convert
***
Генератор
***
filter_by_currency - функция которая возращает интератор
transaction_descriptions - функция-генератордля генерации значений по запросу
card_number_generator - функция-генератор, принимает значение start и stop

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Chaisuu/git_for_python
```
1. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Создайте новый проект и начните добавлять задачи.
3. Назначайте сроки выполнения и приоритеты для задач, чтобы эффективно управлять проектами.

## Документация:

Для получения дополнительной информации обратитесь на почту qwerty@1234.com

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).
