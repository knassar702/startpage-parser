# startpage-parser
parsing search results from startpage search engine (based on google.com results)


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

<img src="https://i.ibb.co/YphfFjj/2.png" alt="2" border="0">
<img src="https://i.ibb.co/wW9WPmb/3.png" alt="3" border="0">
