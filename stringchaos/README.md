## WHAT THE F IS GOING ON
The simple answer: It outputs _"Hello World!"_.

The longer answer: Yeah okay, it isn't a simple _"Hello World!"_ program you find on the internet.  
It is one of the worst implementations you possibly can achieve.  

### So how is it working? (Simple overview)
If you want to write and output _"Hello World!"_, you have to write it in **Base-LOL**.  
**L1B1D2D2E2R2Q1E2F2D2B0S0** is equal to **Hello World!**.  

It is my implementation of **"Base 3"**. It begins with **A0** and after 5 iterations we're 
ending with **B1**.  

| 0 | A0 |
|---|----|
| 1 | A1 |
| 2 | A2 |
| 3 | B0 |
| 4 | B1 |
| 5 | B2 |
| 6 | C0 |  

So you got plenty of room for storing data! ...  
Nah, I lied. You're limited to 3*26=78 possibilities to store data. If you try to use more than
78 registers, you get a **BaseLOLOutOfBounds** exception.  

But... what now? How does it convert to letters?  
That's the neat part! I'm querying a couple of DNS servers with an IP, to get the hostname.
If I got the hostname, I hardcoded the position of the desired letters, 
till I got the alphabet done.  

But finding hostnames for the letters "X, Q, Z" and so on was difficult. Because nearly the whole
web uses Akami, Microsoft, Amazon and Fastly. Plus, I was lazy to search for more hostnames.
So I filled the missing spots with the build-in **string** library. And made it a bit laborious.

After I build a basic dictionary and hardcoded the lowercase letters, I generated dynamically an
uppercase version of the dictionary and joined all dictionaries.  

With that complete dictionary, we're able to print some words, using **Base-LOL**.  

### How does it work? (Technical Explanation)
#### Query
1. Inside the **main.py** you do a query through the **u.query(str)** method.
2. This method does some cleaning. For example:
   1. removing trailing/leading whitespace & linebreaks and whitespace between the characters
   2. checking if the query is even, otherwise it throws an exception
   3. creating pairs of two characters
3. After that, it calls the **_baseLOL_decode(list)** method and pulls the desired letter from the dictionary.  
<br>

#### Base-LOL
The implementation can be found in **/core/baselol.py**. The core method is **baseLOL_locator(int)**, which
determines, based on the given position inside the register, what entry it should return.  
So if you query the position **17** it returns **F1**. So this is how I build the other dictionaries on top of the
base dictionary - that contains the lowercase letters.  

The boundaries are determined dynamically, based on 
**(length of the ascii alphabet)** * **(length of the allowed digits)**.  
<br>

#### Big Dic(tionary)
Inside **/res/big_dict.py** happens the really weird work.  
I declared _"buckets"_, which are holding the hostnames. 
Resolved via the **u.lookup_hostname(str)** method. After that, I just hardcoded the exact positions 
of the letters I wanted, and stored them inside the dictionary **register_l_dict**.  

Since not all hostnames contained the letters "Q, W, X, Z, ...", I added them and filled the gaps.
But now I'm missing an uppercase version of the dictionary, and I don't want to do the manual work again!
So I build it dynamically via the **u.bigd_gen_upper(dict)** method.  
<br>

#### Documentation
I documented every function, that isn't obvious at first glance, so you can dig through it.  
A _"cheat sheet"_, how the letters are assigned, can be found in **/doc/bdict.md**

