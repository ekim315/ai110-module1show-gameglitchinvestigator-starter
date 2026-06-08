# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?  
*The game looked normal; it says make a guess and there's a window you can input a number. I pressed enter or submit guess.*
- List at least two concrete bugs you noticed at the start(for example: "the hints were backwards").  
*The first bug is no change in attempts sometimes when I input a number.  
Another bug I noticed is there is no error when I put a number out of range (ex] -10 or 200).*

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 100   | yes/or go lower   | output go higher| none                   |
| 88    | yes/go higher/lower| no response    | attempts left didn't change
| 200   | error msg         | no response     | none                   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?  
*I used Claude extension in VS Code.*
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).  
*Something AI was right about is that there were many glitches in app.py, especially the high/low logic error.*
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).  
*There wasn't anything so far that AI was wrong about, but I did have to guide it so that it only makes the changes I want at the moment, not additional fixes that I didn't approve of.*

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?  
*I concluded a bug was really fixed if I ran it myself on the application and it didn't output incorrectly.*
- Describe at least one test you ran (manual or using pytest)and what it showed you about your code.  
*I added a pytest via agent to assert if an input is actually higher or actually lower than the guess and to also check if the string in the message corresponds to the correct out come as well.*
- Did AI help you design or understand any tests? How?  
*AI helped me design the pytest for the explanation above. I emphasized to make sure that the message corresponds to the actual hint, and not just the hint being right.*

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?  
*Streamlit most likely reflects changes once it is made in the database. Since it's hosted locally, there is not much wait time for it to load and reflect changes.*

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.  
*One habit to keep is to double check all work that AI has made and converse back and forth about the understanding of why it made those changes and how it applied the changes I wanted.*
- What is one thing you would do differently next time you work with AI on a coding task?  
*One thing I would do differently is to prompt more specifically. When I first asked for assistance, it just listed all suspected bugs in the application, which is not what I wanted since I wanted to find the bugs myself first.*
- In one or two sentences, describe how this project changed the way you think about AI generated code.  
*This project made me realize how far AI has come. When I was using AI for homework assistance or code checks only a year or two ago, I took it with a grain of salt because I would find many errors. Now, it does a great job of curating code the way the user wants it and helps accomplish those specific goals, which I am very surprised about.*
