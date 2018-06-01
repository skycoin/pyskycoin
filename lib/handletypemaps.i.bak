//typedef long long Config__Handle;

/**
*
* typemaps for Wallet Handle
* p0 and p1 as input, unless p1 is after GoString, then it is output
*
**/


/* Join GoString with Wallet__Handle to differentiate from other arguments with Wallet__Handle as p1 */
%typemap(in) (GoString p0, Wallet__Handle* p1) (Wallet__Handle temp) {
	char* buffer = 0;
	int res = SWIG_AsCharPtrAndSize( $input, &buffer, 0, 0 );
	if (!SWIG_IsOK(res)) {
		%argument_fail(res, "(TYPEMAP, SIZE)", $symname, $argnum);
	}
	$1.p = buffer;
	$1.n = strlen(buffer);
	$2 = &temp;
}

/* Add Wallet Handle to result */
%typemap(argout) (GoString p0, Wallet__Handle* p1) {
	%append_output( SWIG_From_long(*$2) );
}

/* Wallet__Handle input typemap. p0 and p1 assume input*/
%typemap(in) Wallet__Handle* p0 (Wallet__Handle temp), Wallet__Handle* p1 (Wallet__Handle temp) {
	SWIG_AsVal_long($input, (long*)&temp);
	$1 = &temp;
}

/* Wallet__Handle not as pointer is input. All input handles should be like this, no pointers */
%typemap(in) Wallet__Handle {
	SWIG_AsVal_long($input, (long*)&$1);
}

/* Wallet__Handle input typemap. From p2 to p7 assume output*/
%typemap(in, numinputs=0) Wallet__Handle* (Wallet__Handle temp) {
	$1 = &temp;
}

/* Wallet__Handle input typemap. From p2 to p7 assume output*/
%typemap(argout) Wallet__Handle* {
	%append_output( SWIG_From_long(*$1) );
}


/**
*
* typemaps for Options__Handle. p0 and p1 input, from p2 to p7 output
*
**/

/* Options__Handle input typemap. From 0 to 1 assume input*/
%typemap(in) Options__Handle* p0 (Options__Handle temp), Options__Handle* p1 (Options__Handle temp) {
	SWIG_AsVal_long($input, (long*)&temp);
	$1 = &temp;
}

/* Options__Handle input typemap. From 2 to 7 assume output*/
%typemap(in, numinputs=0) Options__Handle* (Options__Handle temp) {
	$1 = &temp;
}

/* Options__Handle input typemap. From 2 to 7 assume output*/
%typemap(argout) Options__Handle* {
	%append_output( SWIG_From_long(*$1) );
}

/* Options__Handle not as pointer is input. All input handles should be like this, no pointers */
%typemap(in) Options__Handle {
	SWIG_AsVal_long($input, (long*)&$1);
}

/**
*
* typemaps for general Handle. p0 input, from p1 to p7 output
* handle with no * input of course
*
**/

/* Handle input typemap. From p0 assume input*/
%typemap(in) Handle* p0 (Handle temp) {
	SWIG_AsVal_long($input, (long*)&temp);
	$1 = &temp;
}

/* Handle input typemap. From p1 to p7 assume output*/
%typemap(in, numinputs=0) Handle* (Handle temp) {
	$1 = &temp;
}

/* Handle input typemap. From 1 to 7 assume output*/
%typemap(argout) Handle* {
	%append_output( SWIG_From_long(*$1) );
}

/* Handle not as pointer is input. All input handles should be like this, no pointers */
%typemap(in) Handle {
	SWIG_AsVal_long($input, (long*)&$1);
}

/**
*
* typemaps for general ReadableEntry__Handle. p0 input, from p1 to p7 output
*
**/

/* ReadableEntry__Handle input typemap. From p0 assume input*/
%typemap(in) ReadableEntry__Handle* p0 (ReadableEntry__Handle temp) {
	SWIG_AsVal_long($input, (long*)&temp);
	$1 = &temp;
}

/* ReadableEntry__Handle input typemap. From p1 to p7 assume output*/
%typemap(in, numinputs=0) ReadableEntry__Handle* (ReadableEntry__Handle temp) {
	$1 = &temp;
}

/* Handle input typemap. From 1 to 7 assume output*/
%typemap(argout) ReadableEntry__Handle* {
	%append_output( SWIG_From_long(*$1) );
}

/* ReadableEntry__Handle not as pointer is input. All input handles should be like this, no pointers */
%typemap(in) ReadableEntry__Handle {
	SWIG_AsVal_long($input, (long*)&$1);
}

/**
*
* typemaps for general ReadableWallet__Handle. p0 input, from p1 to p7 output
*
**/

/* ReadableWallet__Handle input typemap. From p0 assume input*/
%typemap(in) ReadableWallet__Handle* p0 (ReadableWallet__Handle temp) {
	SWIG_AsVal_long($input, (long*)&temp);
	$1 = &temp;
}

/* ReadableWallet__Handle input typemap. From p1 to p7 assume output*/
%typemap(in, numinputs=0) ReadableWallet__Handle* (ReadableWallet__Handle temp) {
	$1 = &temp;
}

/* Handle input typemap. From 1 to 7 assume output*/
%typemap(argout) ReadableWallet__Handle* {
	%append_output( SWIG_From_long(*$1) );
}

/* ReadableWallet__Handle not as pointer is input. All input handles should be like this, no pointers */
%typemap(in) ReadableWallet__Handle {
	SWIG_AsVal_long($input, (long*)&$1);
}

/**
*
* typemaps for general WebRpcClient__Handle. p0 input, from p1 to p7 output
*
**/

/* WebRpcClient__Handle input typemap. From p0 assume input*/
%typemap(in) WebRpcClient__Handle* p0 (WebRpcClient__Handle temp) {
	SWIG_AsVal_long($input, (long*)&temp);
	$1 = &temp;
}

/* WebRpcClient__Handle input typemap. From p1 to p7 assume output*/
%typemap(in, numinputs=0) WebRpcClient__Handle* (WebRpcClient__Handle temp) {
	$1 = &temp;
}

/* Handle input typemap. From 1 to 7 assume output*/
%typemap(argout) WebRpcClient__Handle* {
	%append_output( SWIG_From_long(*$1) );
}

/* WebRpcClient__Handle not as pointer is input. All input handles should be like this, no pointers */
%typemap(in) WebRpcClient__Handle {
	SWIG_AsVal_long($input, (long*)&$1);
}

/**
*
* typemaps for general WalletResponse__Handle. p0 input, from p1 to p7 output
*
**/

/* WalletResponse__Handle input typemap. From p0 assume input*/
%typemap(in) WalletResponse__Handle* p0 (WalletResponse__Handle temp) {
	SWIG_AsVal_long($input, (long*)&temp);
	$1 = &temp;
}

/* WalletResponse__Handle input typemap. From p1 to p7 assume output*/
%typemap(in, numinputs=0) WalletResponse__Handle* (WalletResponse__Handle temp) {
	$1 = &temp;
}

/* Handle input typemap. From 1 to 7 assume output*/
%typemap(argout) WalletResponse__Handle* {
	%append_output( SWIG_From_long(*$1) );
}

/* WalletResponse__Handle not as pointer is input. All input handles should be like this, no pointers */
%typemap(in) WalletResponse__Handle {
	SWIG_AsVal_long($input, (long*)&$1);
}


/**
*
* typemaps for general Client__Handle. p0 input, from p1 to p7 output
*
**/

/* Client__Handle input typemap. From p0 assume input*/
%typemap(in) Client__Handle* p0 (Client__Handle temp) {
	SWIG_AsVal_long($input, (long*)&temp);
	$1 = &temp;
}

/* Client__Handle input typemap. From p1 to p7 assume output*/
%typemap(in, numinputs=0) Client__Handle* (Client__Handle temp) {
	$1 = &temp;
}

/* Handle input typemap. From 1 to 7 assume output*/
%typemap(argout) Client__Handle* {
	%append_output( SWIG_From_long(*$1) );
}

/* Client__Handle not as pointer is input. All input handles should be like this, no pointers */
%typemap(in) Client__Handle {
	SWIG_AsVal_long($input, (long*)&$1);
}

/**
*
* typemaps for general Strings__Handle. p0 input, from p1 to p7 output
*
**/

/* Strings__Handle input typemap. From p0 assume input*/
%typemap(in) Strings__Handle* p0 (Strings__Handle temp) {
	SWIG_AsVal_long($input, (long*)&temp);
	$1 = &temp;
}

/* Strings__Handle input typemap. From p1 to p7 assume output*/
%typemap(in, numinputs=0) Strings__Handle* (Strings__Handle temp) {
	$1 = &temp;
}

/* Handle input typemap. From 1 to 7 assume output*/
%typemap(argout) Strings__Handle* {
	%append_output( SWIG_From_long(*$1) );
}

/* Strings__Handle not as pointer is input. All input handles should be like this, no pointers */
%typemap(in) Strings__Handle {
	SWIG_AsVal_long($input, (long*)&$1);
}

/**
*
* typemaps for Wallets__Handle. p0 input, from p1 to p7 output
*
**/

/* Wallets__Handle input typemap. From p0 assume input*/
%typemap(in) Wallets__Handle* p0 (Wallets__Handle temp) {
	SWIG_AsVal_long($input, (long*)&temp);
	$1 = &temp;
}

/* Wallets__Handle input typemap. From p1 to p7 assume output*/
%typemap(in, numinputs=0) Wallets__Handle* (Wallets__Handle temp) {
	$1 = &temp;
}

/* Handle input typemap. From 1 to 7 assume output*/
%typemap(argout) Wallets__Handle* {
	%append_output( SWIG_From_long(*$1) );
}

/* Wallets__Handle not as pointer is input. All input handles should be like this, no pointers */
%typemap(in) Wallets__Handle {
	SWIG_AsVal_long($input, (long*)&$1);
}

/**
*
* typemaps for Config__Handle. p0 input, from p1 to p7 output
*
**/

/* Config__Handle input typemap. From p0 assume input*/
%typemap(in) Config__Handle* p0 (Config__Handle temp) {
	SWIG_AsVal_long($input, (long*)&temp);
	$1 = &temp;
}

/* Config__Handle input typemap. From p1 to p2 assume output*/
%typemap(in, numinputs=0) Config__Handle* p1 (Config__Handle temp), Config__Handle* p2 (Config__Handle temp) {
	$1 = &temp;
}

%typemap(argout) Config__Handle* p0 {
}

/* Handle input typemap. From 1 to 7 assume output*/
%typemap(argout) Config__Handle* p1, Config__Handle* p2 {
	%append_output( SWIG_From_long(*$1) );
}



/* Handle for Config__Handle return parameter for  custom wrapper for SKY_cli_LoadConfig*/
%typemap(out) Config__Handle {
	int error = $1 != 0 ? 0 : -1;
	//Add the error return parameter to be like the other functions
	%append_output( SWIG_From_int(error) );
	//Add handle to return parameters list
	%append_output( SWIG_From_long($1) );
}

/* Config__Handle not as pointer is input. All input handles should be like this, no pointers */
%typemap(in) Config__Handle {
	SWIG_AsVal_long($input, (long*)&$1);
}


/**
*
* typemaps for App__Handle. p0 input, from p1 to p7 output
*
**/

/* App__Handle input typemap. From p0 assume input*/
%typemap(in) App__Handle* p0 (App__Handle temp) {
	SWIG_AsVal_long($input, (long*)&temp);
	$1 = &temp;
}

/* App__Handle input typemap. From p1 to p7 assume output*/
%typemap(in, numinputs=0) App__Handle* (App__Handle temp) {
	$1 = &temp;
}

/* Handle input typemap. From 1 to 7 assume output*/
%typemap(argout) App__Handle* {
	%append_output( SWIG_From_long(*$1) );
}

/* App__Handle not as pointer is input. All input handles should be like this, no pointers */
%typemap(in) App__Handle {
	SWIG_AsVal_long($input, (long*)&$1);
}

/**
*
* typemaps for Context__Handle. p0 input, from p1 to p7 output
*
**/

/* Context__Handle input typemap. From p0 assume input*/
%typemap(in) Context__Handle* p0 (Context__Handle temp) {
	SWIG_AsVal_long($input, (long*)&temp);
	$1 = &temp;
}

/* Context__Handle input typemap. From p1 to p7 assume output*/
%typemap(in, numinputs=0) Context__Handle* (Context__Handle temp) {
	$1 = &temp;
}

/* Handle input typemap. From 1 to 7 assume output*/
%typemap(argout) Context__Handle* {
	%append_output( SWIG_From_long(*$1) );
}

/* Context__Handle not as pointer is input. All input handles should be like this, no pointers */
%typemap(in) Context__Handle {
	SWIG_AsVal_long($input, (long*)&$1);
}

/**
*
* typemaps for Context__Handle. p0 input, from p1 to p7 output
* This should be type mapped as a string map in the target language
**/

/* GoStringMap_ input typemap. From p0 assume input*/
%typemap(in) GoStringMap_* p0 (GoStringMap_ temp) {
	SWIG_AsVal_long($input, (long*)&temp);
	$1 = &temp;
}

/* GoStringMap_ input typemap. From p1 to p7 assume output*/
%typemap(in, numinputs=0) GoStringMap_* (GoStringMap_ temp) {
	$1 = &temp;
}

/* GoStringMap_ input typemap. From 1 to 7 assume output*/
%typemap(argout) GoStringMap_* {
	%append_output( SWIG_From_long(*$1) );
}

/* GoStringMap_ not as pointer is input. All input handles should be like this, no pointers */
%typemap(in) GoStringMap_ {
	SWIG_AsVal_long($input, (long*)&$1);
}

%rename(SKY_cli_LoadConfig) wrap_SKY_cli_LoadConfig2;
%inline {
	Config__Handle wrap_SKY_cli_LoadConfig2(){
		Config__Handle temp = 0;
		if( 0 == SKY_cli_LoadConfig(&temp))
			return temp;
		else 
			return 0;
	}
}


