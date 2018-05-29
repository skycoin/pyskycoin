%{
	PyObject* __add_to_result_list( PyObject *result, PyObject *o ){
		PyObject *o2, *o3, *o4;
		int size;
		if ((!result) || (result == Py_None)) {
			result = o;
		} else {
			if (!PyTuple_Check(result)) {
				PyObject *o2 = result;
				result = PyTuple_New(1);
				PyTuple_SetItem(result, 0, o2);
			}
			o3 = PyTuple_New(1);
			PyTuple_SetItem(o3, 0, o);
			o2 = result;
			result = PySequence_Concat(o2, o3);
			size = PyTuple_Size(result);
			o4 = PyTuple_GetItem( result, size - 2 );
			PyTuple_SetItem( result, size - 1, o4 );
			PyTuple_SetItem( result, size - 2, o );
			//Py_DECREF(o2);
			//Py_DECREF(o3); //TODO: Check why this is failing
		}
		return result;
	}
	
	char* SwigStringToString( PyObject *o ){
		return PyString_AsString( o );
	}
	
	int SwigStringSize( PyObject *o ){
		return PyString_Size( o ); 
	}
	
	PyObject* StringToSwigString( const char* p ){
		return PyString_FromString(p);
	}
	
	PyObject* LongToSwigLong( long int l ){
		return PyLong_FromLong( l );
	}
	
	long SwigLongToLong( PyObject* o ){
		return PyLong_AsLong( o );
	}
	
	
%}
