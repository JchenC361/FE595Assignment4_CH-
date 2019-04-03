                                                                                                                           *****************         
                                                                                                                           *   Handbook  * 
                                                                                                                           *****************
  
1. Save all downloaded male texts in a local folder and save all female text in anothwe local folder.

2. Upload your male and female text data to two separate lists like "HeFileNamesList = os.listdir("D:\He")" and "SheFileNamesList = os.listdir("D:\She")".

3. Run the code in Assignment4.py

5. Open the root directory of the disk where you install python or anaconda. All the files we need to find are in this document.

6. He.txt and She.txt are the files with all the sentences from every file uploaded in Canvas Discusstion. 

7. He_CleanData.txt and She_CleanData.txt are also the files which include all the text tiles saved in Canvas Discusstion.  However, compared to He.txt and She.txt, data in these
two files has been cleaned. The incorrect usage of interpunction has been modified and the sentences has been sorted based on the value of "compound" attribute created by
nltk analyzer from small to large.

8. He_mostCommonSentences.txt and She_mostCommonSentences.txt save the most common descriptions for male character and female character. Since no sentence appear
more than twice, all the sentences save in these two files are the descriptions which appear twice in He.txt or She.txt.

  