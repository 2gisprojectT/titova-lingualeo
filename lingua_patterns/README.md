Тестовый файл Test1
проверяются следующие сценарии:
1) Метод test_Search_NotEmpty - осуществляет поиск значения, которое точно есть в базе данных.
2) Метод test_Search_Empty- осуществляет поиск значения, которого точно нет в базе данных.Проверяет, 
что при отсутствии значения в базе выдает соответствующее сообщение.
3) test_Search_DropFilter - осуществляет поиск значения, которого точно нет в базе данных, затем, при выдаче сообщения, сбрасывает
данный фильтр, переходит ко всем темам.\
4) test_Choose_material - проверяет выборку тем, по заданному фильтру "тип сложности темы" (средний).