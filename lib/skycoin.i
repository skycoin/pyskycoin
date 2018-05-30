%module skycoin
%include "typemaps.i"
%{
	#define SWIG_FILE_WITH_INIT	
	#include "../include/libskycoin.h"
%}

%include "simpletypes.i"
%include "handletypemaps.i"
%include "gostrings.i"
%include "goslices.i"
%include "structs.i"

%include "include/libskycoin.h"




