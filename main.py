from requests import *
from rich.table import Table
from rich.console import Console

res = get("https://www.cbr-xml-daily.ru/daily_json.js")
# print (res.json()["valute"]["AUD"])


table = Table(title="Курсы валют")
table.add_column("Name", style="red")
table.add_column("Value", style="blue")
table.add_column("CharCode", style="yellow")
table.add_column("Nominal", style="green")

for i in res.json()['Valute'].values():
    table.add_row(i['Name'], f'{i['Value']}',  f'{i['CharCode']}',  f'{i['Nominal']}')

    

console = Console()
console.print(table)























