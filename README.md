# makeX
A Python script for Apache servers to make Python executeable.  
Usage: `python3 makeX?.py input.py output.py`  
Each makeX version builds on previous ones.
+ makeX1: For basic execution. No POST, no GET. Good for programs without input.
+ makeX2: Provides the _POST and _GET dictionaries. Does not render "%xx" except "%0D%0A" (\r\n) as \n. Use makeX3 instead.
+ makeX3: Renders "%xx" and adds _status.
   _status(dct,value) returns True if value is a "flag", returns a str if value is an input, and returns False if value is nonexistent.
+ makeX4: Adds _goto.
   _goto(link[, reDir(simulate ridirect?)=true[, relative=false]]) changes the current address.
+ makeX5: Corrects rendering %xx twice.
