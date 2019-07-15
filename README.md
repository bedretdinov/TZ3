ТЗ
========================
### Интерфейс параметров  
<pre> 
--input_file  - Входной файл
--output_file - Вфходной файл
--dT          - Интервал отсечения
</pre>

 
### Сборка
```bash
docker-compose up 
```
### Выполнение
```bash
docker-compose exec  main python3 /app/main.py --dT=0.3 --input_file=test.csv  --output_file=output.csv 
```
 
 
### Пояснение
Была произведена индексация по категриным признакам feature1 и feature2   
При M=100 и более скрипт работает быстро ввиду быстрого поиска засчен большлго количества индексов

![alt demo](https://github.com/bedretdinov/TZ3/Diagram.png)


## Также есть файл main бинарник написанный на GO


### Выполнение
```bash
docker-compose exec main ./main 0.3 incidents.csv outgo.csv 
``` 