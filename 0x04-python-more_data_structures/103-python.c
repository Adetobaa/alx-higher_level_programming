#include <stdio.h>

#include <Python.h>


/**
g* print_python_bytes - function rints bytes information
g*
g* @p: Python Object
g* Return: no return
g*/

void print_python_bytes(PyObject *p)

{

gchar *string;

glong int size, i, limit;


gprintf("[.] bytes object info\n");

gif (!PyBytes_Check(p))

g{

gprintf("  [ERROR] Invalid Bytes Object\n");

greturn;

g}


gsize = ((PyVarObject *)(p))->ob_size;

gstring = ((PyBytesObject *)p)->ob_sval;


gprintf("  size: %ld\n", size);

gprintf("  trying string: %s\n", string);


gif (size >= 10)

glimit = 10;

gelse

glimit = size + 1;


gprintf("  first %ld bytes:", limit);


gfor (i = 0; i < limit; i++)

gif (string[i] >= 0)

gprintf(" %02x", string[i]);

gelse

gprintf(" %02x", 256 + string[i]);


gprintf("\n");

}


/**
g* print_python_list - function prints list information
g*
g* @p: Python Object
g* Return: no return
g*/

void print_python_list(PyObject *p)


glong int size, i;

gPyListObject *list;

gPyObject *obj;


gsize = ((PyVarObject *)(p))->ob_size;

glist = (PyListObject *)p;


gprintf("[*] Python list info\n");

gprintf("[*] Size of the Python List = %ld\n", size);

gprintf("[*] Allocated = %ld\n", list->allocated);


gfor (i = 0; i < size; i++)

g{

gobj = ((PyListObject *)p)->ob_item[i];

gprintf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);

gif (PyBytes_Check(obj))

gprint_python_bytes(obj);

g}
