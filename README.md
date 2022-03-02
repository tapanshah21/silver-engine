# silver-engine
## Purpose
This document briefly explains my approach

## Approach
I am attaching two different files as part of this exercise

`remove_duplicates_and_preserve_order.py`

`remove_duplicates_100k_performance.py`

The code in remove_duplicates_and_preserve_order.py function proves that the functionality works with a smaller sample size. It prints out the list so that one can clearly see that the function removes duplicates while preserving the insertion order. The reason I do this is because printing an entire list of 100000 emails will make the display really hard and difficult to make sense. Hence, the first piece of code is a simpler version that proves that the logic is as expected.

The second function remove_duplicates_100k_performance.py actually does all the legwork and generates 100000 emails with 50000 duplicates. It then proceeds to remove the duplicates while preserving the order and then it calculates the time taken to process it. It prints out the length of the original list, length of the list without duplicates and time taken to process it. Additionally, I run it 10 times to prove that the function consistently processes 100000 email addresses in well under a second.

## Executing the code
The quickest way to check the code would be to use an online editor like https://tio.run/#python3
Alternatively, download both the .py files, make them executable via chmod +x command, and run them locally with the following command like

`python3 filename.py` (assumption here is that user is using a macOS device and has python3 installed)
