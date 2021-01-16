# Word Games Project


### The Q-U Quiz

This problem asks to compute answers for the Q-U Quiz as heard on the
Sunday Puzzle on NPR. The puzzle definition and the radio
broadcast of it can be found here:

  https://www.npr.org/2020/11/08/932548059/sunday-puzzle-the-q-u-quiz

Write a function `qu_quiz` with the following type:

```
string -> (string * string) list
```

This function takes in the name of a file containing a list of words
and produces a list of answers. Each answer is a pair such that if
the letters 'q' and 'u' are added to the first word, the letters can
be rearranged to spell the second word in the pair.

#### Word list
There are 3 word lists given:
- `words-small.txt`
- `words-google-10000.txt`,
  taken from here: https://github.com/first20hours/google-10000-english
- `words-corncob.txt`,
  taken from here: http://www.mieliestronk.com/wordlist.html

#### Sample results

With the sample solution to this problem, evaluating `qu_quiz
"words-small.txt"` will produce the following results:

```
[ ("crooner", "conqueror");
  ("italy", "quality");
  ("stir", "squirt");
  ("teens", "sequent")
]
```
The above text is reformatted to make it easier to read.

The order of word pairs in the list does not matter. Tests of the
functionality of the function will have the following form that only
checks for list membership of answers:
```
List.mem ("italy", "quality") (qu_quiz "words-small.txt")
```
This expression should evaluate to `true`.



### It Takes Two

This problem asks to compute answers for the It Takes Two puzzle
as heard on the Sunday Puzzle on NPR. The puzzle definition and the
radio broadcast of it can be found here:

  https://www.npr.org/2018/01/21/579110492/sunday-puzzle-it-takes-two


Write a function `it_takes_two` with the following type:

```
string -> (string * string) list
```

This function takes in the name of a file containing a list of words
and produces a list of answers.  

Each answer is a pair such that the first string is a 4 letter word
found in the input file and the second is a 6
letter work, also found in the input file, that is created from the 4
letter word by adding a single letter at the front of the word and a
single letter at the end of the word.

The same word files described above in the QU Quiz problem will also
be used for this problem.

For example, the file "words-small.txt" contains "planet" and "lane"
and thus ``it_takes_two words-small.txt`` will return a list
containing `("lane", "planet")`

``answers`` will return the string ``"planet"`` in its output.

With the sample solution to this problem,
evaluating `it_takes_two "words-small.txt"` will produce the following
results:
```
[("lane", "planet"); ("moot", "smooth"); ("hang", "change");
 ("went", "twenty"); ("nigh", "knight"); ("tree", "street");
 ("refi", "prefix"); ("brad", "abrade"); ("awes", "rawest");
 ("onto", "wonton"); ("craw", "scrawl"); ("isle", "misled");
 ("rest", "presto"); ("plan", "upland"); ("afar", "safari")]
```

The order of word pairs in the list does not matter. Tests of the
functionality of the function will have the following form that only
checks for list membership of answers:
```
List.mem ("lane", "planet") (it_takes_two "words-small.txt")
```
This expression should evaluate to `true`.
