
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L15-2 Fun CS Stuff!
# 
# Learner objectives for this lesson
# * Identify something in CS (beyond CptS 111) that interests you
# * Make a plan to continue your CS education
# * Encourage others to learn to code

# ## Overview
# Today we are going to cover various CS-related topics. If anything presented today interests you, please look into it further! Hopefully you will be motivated to continue your CS education and maybe get an idea for a fun side project to work on over winter break.

# ## Visits from WSU EECS Students
# * WSU App Development Club
# * Tyler Walker from [WSU ACM](http://acm.eecs.wsu.edu/#/main)
# * Demietrich Baker and Jordan Little presenting their senior design project

# ## Python
# ### Look How Far We Have Come!
# 1. First day of class "Bingo" ice breaker follow up questions:
#     1. How could you store the above card data on a computer?
#         1. An individual student's card
#         1. All of the cards from each student in the class
#     1. Given an individual card's data, stored in the method you came up with for question 1, how could you algorithmically determine if the card is a winner?
#         1. Fixed size (5x5)
#         1. Variable size (NxN), where N is a positive whole number (N=1,2,3,...)
# 1. Lab1 Task0: `print("Hello CptS 111!")` and BMI calculator
# 1. [PA1 Chatbot](http://nbviewer.jupyter.org/github/gsprint23/cpts111/blob/master/progassignments/PA1.ipynb)
# 1. Our "first program" on the second day of class:
# 
# ```
# print("Please enter the radius of a cone")
# radius = float(input())
# print("Please enter the height of a cone")
# height = float(input())
# 
# volume = 1 / 3 * 3.14 * radius ** 2 * height
# 
# print("The volume of a cone with radius %.2f and height %.2f is %.2f" %(radius, height, volume))
# ```
# 
# ### CS Education Week
# December 5-11, is [CS Education Week](https://csedweek.org/). Share your knowledge of Python by teaching someone (friend, family member, neighbor, etc.) to code in Python! 
# 
# ### Additional Python Resources
# 1. [Python summary sheet](http://www.cs.uni.edu/~fienup/cs1520s14/pythonSummary.pdf)
# 1. There are several tutorials online to learn more about Python programming
# 1. There are several project based Python books, such as [Python Playground](https://www.amazon.com/Python-Playground-Projects-Curious-Programmer/dp/1593276044/ref=sr_1_3?s=books&ie=UTF8&qid=1481143418&sr=1-3&keywords=python+projects)
# 1. Running [Jupyter Notebooks](http://jupyter.org/)
# 1. [Running Python from command line](http://pythoncentral.io/execute-python-script-file-shell/)
#     1. Open a command prompt/terminal
#     1. Navigate to a folder with a Python file you want to run (example: test.py)
#     1. At the command prompt type: `python test.py`

# ## Continuing in CS
# ### Classes after CptS 111:
# 1. Program Design and Development (one of):
#     1. [CptS 121 in C](http://eecs.wsu.edu/~aofallon/cpts121/)
#     1. CptS 131 in Java
# 1. CptS 122/132 Data Structures
# 1. CptS 215/223/233 Advanced Data Structures
# 1. And beyond!
# 
# ### Example C code:
# 
# ```C
# /*
# This is a block comment in C
# */
# 
# #include <stdio.h>
# 
# // main entry point for the program
# int main()
# {
# 	int i = 0;
# 	while (i < 5)
# 	{
# 		printf("%d\n", i);
# 		i += 1;
# 	}
# 
# 	for (i = 0; i < 5; i += 1)
# 	{
# 		printf("%d\n", i);
# 	}
# 	return 0;
# }
# ```
# 
# ### Example Java code:
# ```java
# /*
#  * This is a block comment in Java
#  */
# public class Main {
# 	// main entry point for the program
# 	public static void main(String [] args)
# 	{
# 		int i = 0;
# 		while(i < 5)
# 		{
# 			System.out.println(i);
# 			i += 1;
# 		}
# 		
# 		for(i = 0; i < 5; i += 1)
# 		{
# 			System.out.println(i);
# 		}
# 	}
# }
# 
# ```
# 
# ### WSU CS Bachelor's Degrees Offered:
# 1. [BS in CS](https://school.eecs.wsu.edu/academics/undergraduate-program/computer-science/)
# 1. [BA in CS](https://school.eecs.wsu.edu/academics/undergraduate-program/computer-science/) (not as math/science-intensive)
# 1. [BS in Software Engineering](https://school.eecs.wsu.edu/academics/undergraduate-program/software-engineering/)
# 1. [BS in Data Analytics](https://data-analytics.wsu.edu/)
# 
# ### Get Involved!
# #### Join an EECS Club
# Check out the [list of EECS clubs](https://school.eecs.wsu.edu/students/student-clubs/)
# 
# At a minimum, join the [WSU Chapter of the ACM](https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2Fgroups%2Fwsu.acm.chapter%2F)
# 
# #### Crimson Code Hackathon
# Register for the [Hackathon](http://hackathon.eecs.wsu.edu/#/main)!

# ## Internships
# ### Preparing for Internships
# 1. Keep an up to date technical resume
#     1. Sandi Brabb of the [VCEA PPEL office](https://vcea.wsu.edu/ppel/) can help you with this
# 1. Build a [LinkedIn](https://www.linkedin.com/) profile. This only takes 5-10 minutes to create. It is great to have set up so people can find you and you can build your professional network
# 1. Create a personal website
#     1. There are create online tutorials to learn HTML and CSS. Such as this one on [Codeacademy](https://www.codecademy.com/learn/web)
#     1. As an EECS student, you can [host your website](https://support.vcea.wsu.edu/kb/a21/how-to-update-your-eecs-website-in-windows.aspx) for free on our EECS server
# 1. Prepare an [elevator pitch](https://en.wikipedia.org/wiki/Elevator_pitch) for yourself
# 1. Attend careers fairs to observe (this will help build your confidence):
#     1. Dress code
#     1. Others deliver their elevator pitch
#     1. Interaction between recruiters and students
# 1. Practice CS fundamentals (data structures/algorithms)
# 
# ### Finding Internships
# 1. Attend career fairs
#     1. [VCEA Technical Career Fair](https://vcea.wsu.edu/careerfair/) in the Fall
#     1. [WSU Career Expo](https://ascc.wsu.edu/career-expo/) in the Spring
# 1. Attend talks when companies come visit WSU
# 1. Leverage your professional network
# 1. Search/apply online

# ## Undergraduate Research
# 1. [WSU Office of Undergraduate Research](https://undergraduateresearch.wsu.edu/)
# 1. [National Science Foundation (NSF) Research Experience for Undergraduates (REU)](https://www.nsf.gov/crssprgm/reu/)
# 1. [REUs at WSU](https://summerresearch.wsu.edu/research-opportunities/)
#     1. A few in CS are currently accepting applications!
#     1. TA Jackson did an REU at WSU this past summer

# ## Any Further CS-related Questions?
# You can always contact me by email, or stop by my office hours. Other resources include:
# 1. [EECS Advising](https://school.eecs.wsu.edu/people/advisors/)
# 1. [All EECS contacts](https://school.eecs.wsu.edu/contact/)
# 
# Also, if you have any suggestions for improvements to CptS 111, please let me or [Dr. Shira Broschat](https://school.eecs.wsu.edu/people/faculty/shira-broschat/) know!

# ## TODO
# 1. Study for the final
# 1. Keep in touch after CptS 111 ends :)
# 
# ## Next Lesson
# 1. There is no next lesson. Congrats on finishing CptS 111! Have fun in CptS 121!
# 1. Go Cougs!
# 
# <img src="https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/while_true_go_cougs.png" width="400">
