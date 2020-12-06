# Program to perform Shannon Encoding

-   Meant for an assignment, this is a python program that takes a string to encode and returns the code for each symbol in that string
-   The encoding is performed using Shannon Binary encoding. The algorithm for the process is as follows:
    1. Input a string of characters
    2. Compute the frequency of each character, and use that to compute its probability
    3. Sort the list of unique characters, in decreasing order of their probabilties.
    4. Create a list of α<sub>i</sub> values, which is the same as the cumulative sum of each probabilty.
    5. Find the length of each encoded word, using the formula 2<sup>l<sub>i</sub></sup> >= 1/(p<sub>i</sub>)
