# startpage-parser
parsing search results from startpage search engine (based on google.com results)
you can use it if you need get some results without get banned from google

<img src="https://i.ibb.co/pxbCQdm/Untitled-Diagram.png" alt="Untitled-Diagram" border="0" width="600" height="150" align=center>

### INSTALL

* from pip
```
$ pip install startpage-parser
```
* from source
```
$ git clone https://github.com/knassar702/startpage-parser
$ cd startpage-parser
$ pip install -e .
```

***

```python
>>> from startpage import StartPage
>>> task = StartPage()
>>> task.search("Hello World",page=1) # page = number of pages (page=10 > from page number one to page number ten)
>>> # All results stored in .results 
>>> # print(task.results)
>>> # {'page number':"Results"}
>>> print(task.results)
{'1': [{'title': '"Hello, World!" program - Wikipedia', 'link': 'https://en.wikipedia.org/wiki/%22Hello,_World!%22_program', 'description': 'A "'}, {'title': 'Hello World (film) - Wikipedia', 'link': 'https://en.wikipedia.org/wiki/Hello_World_(film)', 'description': <b>Hello World</b>}, {'title': 'hello world - YouTube', 'link': 'https://www.youtube.com/watch?v=Yw6u6YkTgQ4', 'description': '30 Mar 2018 '}, {'title': 'Total immersion, Serious fun! with Hello-World!', 'link': 'https://www.hello-world.com/', 'description': 'Main index for '}, {'title': 'Hello, World! - Learn Python - Free Interactive Python Tutorial', 'link': 'https://www.learnpython.org/en/Hello,_World!', 'description': <b>Hello</b>}, {'title': 'C "Hello, World!" Program', 'link': 'https://www.programiz.com/c-programming/examples/print-sentence', 'description': 'In this example, you will learn to print "'}, {'title': 'C++ "Hello, World!" Program', 'link': 'https://www.programiz.com/cpp-programming/examples/print-sentence', 'description': 'In this example, we will learn to create a simple program named "'}, {'title': "The History of 'Hello, World' - HackerRank Blog", 'link': 'https://blog.hackerrank.com/the-history-of-hello-world/', 'description': '21 Apr 2015 '}, {'title': 'Hello World Studio', 'link': 'https://www.helloworldstudio.org/', 'description': <b>Hello World</b>}, {'title': 'Hello World - Go by Example', 'link': 'https://gobyexample.com/hello-world', 'description': 'To run the program, put the code in '}]}

```

### examples

```python
from startpage import StartPage

task = StartPage()
task.search("Hello World",page=1)
for page_num,results in task.results.items():
    print(f'PAGE: {page_num}\n---------------')
    for res in results:
        print(f'Title: {res["title"]}\n Description: {res["description"]}\n Link: {res["link"]}\n======')
"""
PAGE: 1
---------------
Title: "Hello, World!" program - Wikipedia
 Description: A "
 Link: https://en.wikipedia.org/wiki/%22Hello,_World!%22_program
======
Title: Hello World (film) - Wikipedia
 Description: <b>Hello World</b>
 Link: https://en.wikipedia.org/wiki/Hello_World_(film)
======
Title: hello world - YouTube
 Description: 30 Mar 2018 
 Link: https://www.youtube.com/watch?v=Yw6u6YkTgQ4
======
Title: Total immersion, Serious fun! with Hello-World!
 Description: Main index for 
 Link: https://www.hello-world.com/
======
Title: Hello, World! - Learn Python - Free Interactive Python Tutorial
 Description: <b>Hello</b>
 Link: https://www.learnpython.org/en/Hello,_World!
======
"""
```

<img src="https://i.ibb.co/YphfFjj/2.png" alt="2" border="0">
<img src="https://i.ibb.co/wW9WPmb/3.png" alt="3" border="0">
