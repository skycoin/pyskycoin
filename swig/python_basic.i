%begin %{
#define SWIG_PYTHON_STRICT_BYTE_CHAR
%}

%typecheck(SWIG_TYPECHECK_STRING_ARRAY) GoSlice*  {
  $1 = PyList_Check($input) ? 1 : 0;
}

/*GoStrings* parameter to return as a list */
%typemap(in, numinputs=0) (coin__UxArray* __return_strings) (coin__UxArray temp) {
	temp.data = NULL;
	temp.len = 0;
	temp.cap = 0;
	$1 = &temp;
}

/*GoStrings* parameter to return as a list */
%typemap(in, numinputs=0) (GoSlice* __return_strings) (GoSlice temp) {
	temp.data = NULL;
	temp.len = 0;
	temp.cap = 0;
	$1 = &temp;
}


/*GoStrings* as function return typemap*/
%typemap(argout) (coin__UxArray* __return_strings) {
	int itoken;
	PyObject *list = PyList_New(0);
    GoString *iStr;
   int ntokens = $1->len; 
   PyObject *py_string_tmp; 
   int py_err; 
   for (itoken = 0, iStr = (GoString *) $1->data; itoken< ntokens; ++itoken, ++iStr) {
       if (iStr == NULL) break; 

       /* convert C string to Python string */ 
       py_string_tmp = SWIG_FromCharPtrAndSize((const char *) iStr->p,iStr->n ); 
       if (! py_string_tmp) return NULL; 

       /* put Python string into the list */ 
       PyList_Append(list, py_string_tmp);
       if (py_err == -1) return NULL; 
   } 
	if( $1->data != NULL)
		free( (void*)$1->data );
	%append_output( list );
}

/*GoStrings* as function return typemap*/
%typemap(argout) (GoSlice_* __return_strings) {
	int itoken;
	PyObject *list = PyList_New(0);
    GoString *iStr;
   int ntokens = $1->len; 
   PyObject *py_string_tmp; 
   int py_err; 
   for (itoken = 0, iStr = (GoString *) $1->data; itoken< ntokens; ++itoken, ++iStr) {
       if (iStr == NULL) break; 

       /* convert C string to Python string */ 
       py_string_tmp = SWIG_FromCharPtrAndSize((const char *) iStr->p,iStr->n ); 
       if (! py_string_tmp) return NULL; 

       /* put Python string into the list */ 
       PyList_Append(list, py_string_tmp);
       if (py_err == -1) return NULL; 
   } 
	if( $1->data != NULL)
		free( (void*)$1->data );
	%append_output( list );
}