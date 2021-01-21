cd D:\Auto_test_python\TP_Api_Test\report\tmp
del *.json
cd D:\Auto_test_python\TP_Api_Test\test_case
pytest test_Data_Index.py -sq --alluredir=../report/tmp
allure generate ../report/tmp -o ../report/report --clean
pause
