## Project: Meta Analyser Tool

This directory contains some files that are useful for the implementation of the project of the course. In particular:

* The file [`mat.py`](https://comp-think.github.io/2019-2020/project/mat.py) contains the implementation of the class `MetaAnalyserTool` that has been presented during the course. You have to reuse it as it is without modifying anything except the import statement which is declared in the very first line. Currently, it is importing all the functions defined in another file, i.e. `my_test_group.py`, which is a stub implementation of the functions you have to implement for developing the project - see next point.
* The file [`my_test_group.py`](https://comp-think.github.io/2019-2020/project/my_test_group.py) is a stub implementation containing the signature (i.e. the functions definition without any code in it) of all the functions you have to implement. These functions are then reused in the class `MetaAnalyserTool`. Of course it is possible to add even additional functions to this file if you want. The only important thing is that the seven functions used in the aforementioned class are defined.
* The file [`execution_example.py`](https://comp-think.github.io/2019-2020/project/execution_example.py) is an example of how I will use the class `MetaAnalyserTool` (and, thus, your code) for testing the various methods for searching and providing data. You can use similar instruction to test the various methods of the class that have been implemented by means of your functions. Of course, you are free to run additional (and even complex) search queries so as to properly test your project. The instruction contained in this file can be run by using the Python 3 interpreter in the shell (`python3 execution_example.py`). Note that currently the class does not work as expected since it is using the functions implemented in `my_test_group.py`, that return *None*.
* The file [`metadata_sample.csv`](https://comp-think.github.io/2019-2020/project/metadata_sample.csv) is the comma-separated value (CSV) document containing a sample of the data that will be used in the evaluation of your project. It is a quite small (but complete) dataset, that allows you to test properly your project.
 
 For your convenience, you should download all these files and put them in the same directory. It is worth mentioning that the description of all the functions is already provided in the [slides that introduce the project](https://comp-think.github.io/2019-2020/slides/14%20-%20Project.html). You can use the information contained there as the official documentation of the various functions.
 
 As a reminder, your project (i.e. the implementation of the seven functions including any additional ancillary function developed, if any) must be included in a single file named after your group - e.g. I used `my_test_group.py` which represents my fictional group (i.e. *My Test Group*) in the aforementioned examples. Your file should be sent by email to [silvio.peroni@unibo.it](mailto:silvio.peroni@unibo.it), from your University email account, two days before the exam session session - e.g. you have to send the project by the 28th of January 2020 for discussing it in the session of the 30th of January 2020. As a general rule, all the members of the group must attend the session - no exception.