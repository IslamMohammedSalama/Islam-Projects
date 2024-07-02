
CC = clang

CFLAGS = -I$(HOME)/local/include

LDFLAGS = -L$(HOME)/local/lib -lcs50

hello: hello.c 
	$(CC) $(CFLAGS) -o hello hello.c $(LDFLAGS)

clean:
	rm -f hello