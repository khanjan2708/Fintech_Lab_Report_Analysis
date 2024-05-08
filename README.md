# Fintech_Lab_Report_Analysis

Let Me Breakdown the steps I did for the task:
1. I first wrote code for the scraping of SEC-EDGAR 10-K Annual report
2. After this I wrote code for the Text analysis of it reports. (This code Summarizes the report and gives insight)

## Scraping of 10-K Annual Report
I used sec_edgar_dowanloader library to download 10-K report from the website.As it was mentioned that we need to extract 10-K reports from 1995 to 2023. If Company has IPO after 1995 then from that IPO year to 2023.

To get details about companies I used yfinance library and got historical data and the first index of that data is the IPO date. From there I extracted the year of IPO.

Using this I got Reports in .txt format in a local Folder downloaded.
I downloaded two companies NVIDIA AND WeWork as One company has seen very faast growth due to technology boost and other company due to bad Management has been faced fall. While it was one of the fastest growing startup in 2020 - 2021.

## Text Analysis of the Report
I was only able to write a code such that it considers one report at each time. It took me so long to figure out the use of LLM APIs. 
I used Gemini API (to be precise gemini-1.0-pro) for the Analysis.
So now talking about Report the report is of Format .txt but even so the text inside it so much of HTML while the header is Text which contains details of Company, its filing date, address etc.

Read_txt_file : Function to open file and use it in code as a string
get_text_from_candidate : This function take response candidate in as arguement and extracts only the answer which is text part of it and returns it. As the response candidate contains many other parameters which is not much of our use.

After this as I said the text file first contains some company information and after it has HTML format. So I built this function:
extract_company_info(text) : Takes text document as an arguement
First divides the report in two parts the part that contains info of company and HTML which is satrt from the <HTML> tag.
After dividing this the company info is fed to model to generate content.|Using prompt name of company and date of filing is extracted using prompt and Regex library.

![image](https://github.com/khanjan2708/Fintech_Lab_Report_Analysis/assets/127283590/27c04aae-3905-49a6-be22-47b6ba22b752)

After this made a function which is combine_text : Thid function preprocesses the text which is extracted from html parsed. This contains some forms like \xao and \n so This function replaces \xa0 with ' ' and if there is '\n\n\n' then it gives paragraph from there. This processed text is the return of the function.

After this using beutiful Soup Library the text from HTML part of the file is extracted. Using Natural Language Tool Kit(nltk) library the text is been tokenized.

Now comves the IMP part of the text analysis:
Now The text is too long for any LLM to process so I needed it to be sectioned in groups which are so much relevant for us to use:
Business Model / Business
Financial Statements
Management Decisions
Risk Factors
Others : To contains which may be relevant but not part of the above sections.

process_batch : This function takes arguement of batch, sections, section_dictionary (where I will store the sectioned text).
In this function I have prompt which tells LLM to classify in section by providng one word output and then using NLP like regex to find pattern and append it to that dictionary which has same section name.
This is how function is built to divide the whole report in sections.
After this using join function I joined sentences to create a paragrapgh.

Using Function Summarize_with_gemini function : Using two prompts One to summarize the report and second to note down important thing. Using this function I got summary and IMP things as a response.

Now I used this function on different section of the dictionary and for specifically two sections ['Business' and 'Financial Statement'] I have asked three-two questions like
For business : Insigh contains what is the product company has, what are competitors, plan for expansion, Market
For Finacial Statement : Insight contains some important numerical values associated with it, Like Revenue, CapEx, Investment, Cash Flow etc.
So using this kind of prompts and API I extracted some insights from the report.

How will user benefit from the insight:
It will have management decision and Business Expansion plans so it helps in taking decision for investment as this decision affect the companies growth affectively.

Gives insight of Financial Data so it becomes easy to compare the results and to overview the growth.












