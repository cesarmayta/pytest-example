#comandos
pip install pytest

pytest --ejecuta todas las pruebas
para ejecutar solo una prueba
pytest -v muestra mas detalle

pytest test_main.py::TestExample::test_resta_dos_numeros -v
ejecuta una prueba en especifico

pytest -s #muestra mensajes print
