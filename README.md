# Guess_the_rank
0. The data is taken from the website of Riot Games. You can find and pull it from here: https://developer.riotgames.com/apis
   
1. Please note that the prediction is given by using linear regression and ridge regression

2. The reason why we guess the rank is sometimes, their rank does not reflect their true ability. (maybe smurfing - when skilled players tend to wreck the noobs )

3. The file data.csv is compiled from the files within Processed_Final_Data and also, it was added the label of rankings as integers. (The code for this step is missing :( )

- For example, the lowest rank is Iron which was encoded to 0, Silver to 1, ..., Challenger as the highest to 8
<div align="center">
  
![image](https://github.com/user-attachments/assets/25bc5fff-52f0-4dc1-a6a8-04713988dcac)

![image](https://github.com/user-attachments/assets/77bba1b0-3014-4e9c-87cb-2f87e733c698)

![image](https://github.com/user-attachments/assets/98bb8118-9f0c-432d-967b-f6593b5a4ea0)
</div>

4. Since this is a group project and we just don't have too much time, the result may dissapoint you guys a bit (final results are just real positive numbers) .

5. If you want to truly see the result, i recommend you to or convert it back to strings from these numbers (you can use floor function) or use this number to guess the rank range they are in

- For example, the point of them is 0.5 => They can be between Iron and Bronze
- Of course, you can think about rounding the numbers of the output, but it can cost some accuracy.
- For example: 0.94 is rounded to 0.9 as Iron while 0.95 can be considered as 1 - Silver
