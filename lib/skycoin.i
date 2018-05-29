%module skycoin
%include "typemaps.i"
%{
	#define SWIG_FILE_WITH_INIT	
	#include "../include/libskycoin.h"
%}

%include "pyutils.i"
%include "handletypemaps.i"
%include "gostrings.i"

%include "include/libskycoin.h"




