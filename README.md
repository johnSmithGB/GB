### Запустить lesson1:
- pip install -r requirements.txt
- gunicorn app:app


- файл data.yaml: slug страниц, handler и название ссылок в меню
- папка models: данные для моделей в формате yaml
- templates: базовый шаблон, типовой, и индивидуальный(используетcя PageController) + шаблон инлайновых стилей css