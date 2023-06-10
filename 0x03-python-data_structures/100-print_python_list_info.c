void print_python_list_info(PyObject *p)
{
Py_ssize_t size = PyList_Size(p);
    printf("List size: %zd\n", size);

    printf("List elements:\n");
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        PyObject *repr = PyObject_Repr(item);
        const char *str = PyUnicode_AsUTF8(repr);
       
        if (PyLong_Check(item)) {
            printf("%zd (int): %s\n", i, str);
        } else if (PyFloat_Check(item)) {
            printf("%zd (float): %s\n", i, str);
        } else if (PyUnicode_Check(item)) {
            printf("%zd (str): %s\n", i, str);
        } else {
            printf("%zd (unknown): %s\n", i, str);
        }
       
        Py_XDECREF(repr);
    }
}
