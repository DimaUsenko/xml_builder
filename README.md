## Структура проекта
```bash
├── app.py  # Ручка запуска приложения
├── Makefile  # Сбилдить окружение и запустить приложение
├── README.md
├── templates 
│   ├── data-graph.png  # То, что должно получаться в виде графа
│   └── template.xml  # То, что должно получаться
├── validators.py  # Здесь пишем функции для проверок полей данных
└── venv
```

## ToDo
Сейчас в качестве примера описаны ```Message``` и ```Organization```(см код и [data-graph.png](templates/data-graph.png)). 
Надо 
1. Описать все оставшиеся сущности, которые формируют выходной XML, а именно: 
   1. Forms
   2. Form8
   3. ContractSpending 
   4. Contractors.Contractor
   5. PlannedPay
   6. ContractFinance
   7. Supplement
   8. Part
   9. Reasons
2. Написать все необходимые функции валидации (см. пример валидации [validators.py](validators.py))

## Примечаения

  Здесь самое главное - просто собрать через формы все необходимые поля (Вероника) и провалидировать их (Саша).