#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		int fib();
		void set(int);
	private:
		int val;
		int _fib(int);
	};
 
Integer::Integer(int n){
	val = n;
	}

int Integer::fib(){ 
	return _fib(int val);
	}

int Integer::_fib(int n)
{
    if (n <= 1)
        return n;
    return _fib(n-1) + _fib(n-2);
}

// This code is cont
int Integer::get(){
	return val;
	}
 
void Integer::set(int n){
	val = n;
	}


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_fib(Integer* integer) {return integer->fib();}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}