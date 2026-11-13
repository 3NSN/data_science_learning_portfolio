import json

# 1. Открываем и читаем наш JSON файл
with open('sentry_weekly_export.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

issues_list = data['issues']
filtered_issues = []

# 2. Фильтруем баги (собираем подходящие в новый список)
for issue in issues_list:
    # Обращаемся к значениям по ключам словаря
    if issue['status'] == 'unresolved' or issue['affected_users'] > 100:
        filtered_issues.append(issue)

# 3. Сортируем записи от большего к меньшему количеству 'affected_users'
# Используем лямбда-функцию, чтобы указать, по какому именно ключу сортировать
filtered_issues.sort(key=lambda x: x['affected_users'], reverse=True)

# Берем только Топ-3 для отчета, чтобы не спамить в чат
top_issues = filtered_issues[:3]

# 4. Формируем красивый текст и записываем в файл
message_lines = ["🚨 *Weekly Sentry Crash Report - Top 3 Critical Issues* 🚨\n"]
for i, bug in enumerate(top_issues, 1):
    line = f"{i}. {bug['error_type']} in {bug['location']} ({bug['platform']}) - {bug['affected_users']} users affected"
    message_lines.append(line)

final_message = "\n".join(message_lines)

# Создаем файл slack_message.txt и записываем туда текст
with open('slack_message.txt', 'w', encoding='utf-8') as msg_file:
    msg_file.write(final_message)

print("✅ Файл slack_message.txt успешно создан!\n")


# 5. Функция-заглушка для заведения багов в Jira
def create_jira_ticket(bug):
    # В реальном проекте здесь был бы вызов requests.post('https://jira.vinted.com/rest/api/...', json={...})
    print(f"[JIRA API] Заведен баг-репорт для {bug['error_type']} на {bug['platform']} (Ticket: VNT-101)")

# Заводим баги на каждый пункт в полученном списке
for bug in top_issues:
    create_jira_ticket(bug)


# 6. Отправляем файл сообщением в Slack
def send_to_slack(text):
    # В реальности использовался бы Slack Webhook:
    # webhook_url = "https://hooks.slack.com/services/T0000/B0000/XXXXX"
    # requests.post(webhook_url, json={"text": text})
    print("\n[SLACK API] Сообщение успешно отправлено в канал #dev-alerts!")
    print("-" * 40)
    print(text)
    print("-" * 40)

send_to_slack(final_message)