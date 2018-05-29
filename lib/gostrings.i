typedef struct{
	char* p;
	int   n;
} GoString;

typedef struct{
	char* p;
	int   n;
} GoString_;


/*GoString in typemap*/
%typemap(in) GoString {
	$1.p = SwigStringToString( $input );
	$1.n = SwigStringSize( $input ); 
}

/*GoString_* parameter as reference */
%typemap(in, numinputs=0) GoString_* (GoString_ temp) {
	temp.p = NULL;
	temp.n = 0;
	$1 = &temp;
}

/*GoString_* as function return typemap*/
%typemap(argout) GoString_* {
	$result = __add_to_result_list( $result, StringToSwigString( $1->p ) );
	free( (void*)$1->p );
}
