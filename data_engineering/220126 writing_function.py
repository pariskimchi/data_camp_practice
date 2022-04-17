

# open "alice.txt" and assign the file to "file"


path = "alice.txt"

with open(path) as file:
    text = file.read()

n  = 0
for word in text.split():
    if word.lower() in ['cat','cats']:
        n +=1
print('cat {} times'.format(n))



# The "yield" keyword 


@contextlib.contextmanager 
def my_context():
    print('hello')
    yield 42 
    print('goodbye')

with my_context() as foo:
    print('foo is {}'.format(foo))


# Yielding a value or None 

@contextlib.contextmanager 
def database(url):
    # set up database connection 
    db = postgres.connect(url)

    yield db 

    # tear down database connection 
    db.disconnect()


url = 'https://datacamp.com/data'
query = "SELECT * FROM courses"
with database(url) as my_db:
    course_list = my_db.execute(query)


# Path 

@contextlib.contextmanager 
def in_dir(path):
    #save corrent working directory 
    old_dir = os.getcwd()

    # switch to new working directory 
    os.chdir(path)

    yield

    # change back to previous 
    # working directory 
    os.chdir(old_dir)

# run 
path = '/data/project_1/'

with in_dir(path):
    project_files = os.listdir()


# Nested contexts 
def copy(src, dst):
    """Copy the contents of one file to another.

    Args:
        src (str): file name of the file to be copied
        dst (str): where to write the new file.
    """
    # open the source file and read in the contents 
    with open(src) as f_src:
        contents = f_src.read()

    #open the destination file and write out the contents 
    with open(dst, 'w') as f_dst:
        f_dst.write(contents)
    

# correct 

def copy(src, dst):
    """Copy the contents of one file to another
    
    Args:
        src (str): File name of the file to be copied 
        dst (str): where to write the new file.

    """
    # open both files 
    with open(src) as f_src:
        with open(dst,'w') as f_dst:
            # REad and write each line, one at a time 
            for line in f_src:
                f_dst.write(line)


# Handling Errors 

def get_printer(ip):
    p = connect_to_printer(ip)

    try:
        yield 
    finally:
        p.disconnect()
        print('disconnected from printer')

doc = {'text':'this is my text.'}

with get_printer('10.0.34.111') as printer:
    printer.print_page(doc['txt'])