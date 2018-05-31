%extend cipher__Address {
	int isEqual(cipher__Address* a){
		if( $self-> Version == a->Version ){
			for(int i = 0; i < 20; i++)
				if( $self->Key[i] != a->Key[i] )
					return 0;
			return 1;
		}
		return 0;
	}
}

%extend cipher_SecKeys {
	cipher_SecKey* getAt(int i){
		if( i < $self->count ){
			return &$self->data[i];
		}
		else 
			return NULL;
	}
}

