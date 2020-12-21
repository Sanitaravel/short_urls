# Мини-проект "Сокращатель ссылок":
(1) Александр
- обработчик store, который вызывается по URL /store/<длинная ссылка>, которое создаёт короткую ссылку по переданной длинной ссылке, а также сохраняет его в глобальный словарь urls вида {short_url_1: long_url_1, short_url_2: long_url_2, ...}
- форма для ввода URL с кнопкой "сгенерировать короткую ссылку".
- страница, отображающая пользователю сгенерированную короткую ссылку
- В идеале сделать генерацию короткой ссылки без перезагрузки страницы при помощи Ajax
- Объединить результаты работы всех участников и запустить на сервере 95.85.18.95. Порт, например, 5001.

(2) Тимофей
- генератор уникальных коротких ссылок -- функция idgen.
  Для её реализации можно воспользоваться библиотекой hashlib или base64.
  И не забыть убедиться, что сгенерированная ссылка уникальна.
- обработчик load, который вызывается по URL /<короткая ссылка>; при переходе по этой ссылке сервер должен отдавать браузеру редирект
- добавить сохранение всей информации в json (функция json.dumps) при изменении информации. Загрузка (json.loads) информации из файла при запуске приложения, при условии, что сохранённые настройки существуют. Схема сохраняемых данных:
{
  "urls": urls,
  "stats": stats, # это только примеры названий полей
    ...
}

(3) Пётр
- Сделать подсчёт статистики переходов по ссылкам. 
  По запросу /stats/<короткая ссылка> должна отображаться информация:
  -- куда эта эта ссылка ведёт
  -- сколько раз пользователи прошли по этой короткой ссылке
Дополнительно:
выводить в статистике короткой ссылки
  -- IP-адреса тех, кто заходил (можно глянуть на ссылку https://stackoverflow.com/a/3760309/10712892)
- По запросу /top_stats?limit=<N> отображать топ-N самых популярных ссылок.

Основной репозиторий принадлежит Саше: https://github.com/Sanitaravel/short_urls
Коллабораторы:
pettum0104 -- Петя
Multus -- Тимофей

Вся работа ведётся в ветках git-а. Стандартный workflow работы: 
git clone <repo_url>
cd repo # не забудьте зайти в проект

git checkout -b branch_name  # создать новую ветку и перейти в неё

git add .  # добавить всю папку в гит
git commit -m "some message"    #  сделать слепок
git push -u origin branch_name  # отправить ветку branch_name на сервер origin

git add files_to_add...  # снова добавляете файлы
git commit -m "some message" # делаете слепок
git add files_to_add...  # снова добавляете файлы
git commit -m "some message" # делаете слепок
git add files_to_add...  # снова добавляете файлы
git commit -m "some message" # делаете слепок

git push # отправляете результат на гитхаб
Затем на сайте гитхаба делаете pull request в ветку master, объединяете изменения, разбираете конфликты версий и делаете merge.


noteid.json format:

```json
    idlist: [
        unic_id: original_link
    ]
```