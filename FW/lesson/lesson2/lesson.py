from jinja2 import Environment, FileSystemLoader

subs = ['Культура', 'Наука', ' Политика', 'Спорт']
persons = [{"name": "Алексей", "year": 18, "weight": 78.5},
           {"name": "Никита", "year": 28, "weight": 82.3},
           {"name": "Виталий", "year": 33, "weight": 94.0}]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render(list_table=subs)
print(msg)
