#include <Python.h>
#include "listobject.h"
void print_python_list_info(PyObject *p);
/**
 * print_python_list_info - ===========
 * @p: ============
 * Description: =====
 * Return: ===========
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	PyObject *item, *repr;
	const char *str;

	printf("List size: %zd\n", size);

	printf("List elements:\n");
	for (i = 0; i < size; i++) 
	{
		item = PyList_GetItem(p, i);
		repr = PyObject_Repr(item);
		str = PyUnicode_AsUTF8(repr);

		if (PyLong_Check(item))
		{
			printf("%zd (int): %s\n", i, str);
		}
		else if (PyFloat_Check(item))
		{
			printf("%zd (float): %s\n", i, str);
		}
		else if (PyUnicode_Check(item))
		{
			printf("%zd (str): %s\n", i, str);
		}
		else if (PyTuple_Check(item))
		{
			printf("%zd (tuple): %s\n", i, str);
		}
		else if (PyList_Check(item))
		{
			printf("%zd (list): %s\n", i, str);
		}
		else if (PyDict_Check(item))
		{
			printf("%zd (dict): %s\n", i, str);
		}
		else if (PyBool_Check(item))
		{
			printf("%zd (bool): %s\n", i, str);
		}
		else if (item == Py_None)
		{
			printf("%zd (None): %s\n", i, str);
		}
		else
		{
			printf("%zd (unknown): %s\n", i, str);
		}
		Py_XDECREF(repr);
	}
}
