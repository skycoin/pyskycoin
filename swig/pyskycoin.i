%module skycoin
%include "typemaps.i"
%{
	#define SWIG_FILE_WITH_INIT
	#include "libskycoin.h"
	#include "swig.h"
	// #include "base64.h"
%}

//Apply strictly to python
//Not for other languages
%include "/gopath/src/github.com/skycoin/skycoin/lib/swig/common/common.i"
%include "/gopath/src/github.com/skycoin/skycoin/lib/swig/dynamic/dynamic.i"
%include "python_skycoin.cipher.crypto.i"
%include "python_uxarray.i"
%include "python_sha256s.i"
%include "python_skycoin.coin.i"
%include "python_skycoin.callback.i"
%include "structs_typemaps.i"
%include "python_basic.i"
%include "skycoin.mem.i"

%include "swig.h"
/* Find the modified copy of libskycoin */
%include "libskycoin.h"
%include "structs.i"
%include "skyerrors.h"
