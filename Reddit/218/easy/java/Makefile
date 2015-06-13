JAVAC = javac
JAVA = java
JAVAC_FLAGS = -Xlint:all

MAIN_CLASS = Easy
SOURCES = Easy.java

# by default (i.e. if no target is specified), 
# use the "compile the source" target
default: $(MAIN_CLASS)

# compile source code into binaries (.class files)
$(MAIN_CLASS): $(SOURCES)
	@echo Building $@...
	$(JAVAC) $(JAVAC_FLAGS) $^ 

# pass driver class object to JRE
run:
	$(JAVA) $(MAIN_CLASS) $(ARGS)

# clean up object files
clean:
	@rm -f $(OBJECTS) 
