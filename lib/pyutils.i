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
			result = PySequence_Concat(o3, o2);
			//size = PyTuple_Size(result);
			//o4 = PyTuple_GetItem( result, size - 2 );
			//PyTuple_SetItem( result, size - 1, o4 );
			//PyTuple_SetItem( result, size - 2, o );
			Py_DECREF(o2);
			Py_DECREF(o3); //TODO: Check why this is failing when swaping items
		}
		return result;
	}
	
	
	
%}
