# data =[{"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#   "question": "French is an official language in Canada.", "correct_answer": "True", "incorrect_answers": ["False"]},
#  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#   "question": "It is automatically considered entrapment in the United States if the police sell you illegal substances "
#               "without revealing themselves.",
#   "correct_answer": "False", "incorrect_answers": ["True"]},
#  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#   "question": "Bulls are attracted to the color red.", "correct_answer": "False", "incorrect_answers": ["True"]},
#  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy", "question": "The Sun rises from the North.",
#   "correct_answer": "False", "incorrect_answers": ["True"]},
#  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#   "question": "The color orange is named after the fruit.", "correct_answer": "True", "incorrect_answers": ["False"]},
#  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#   "question": "You can legally drink alcohol while driving in Mississippi.", "correct_answer": "True",
#   "incorrect_answers": ["False"]},
#  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy", "question": "Pluto is a planet.",
#   "correct_answer": "False", "incorrect_answers": ["True"]},
#  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#   "question": "Adolf Hitler was born in Australia. ", "correct_answer": "False", "incorrect_answers": ["True"]},
#  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#   "question": "One of Donald Trump&#039;s 2016 Presidential Campaign promises was to build a border wall between the United States and Mexico.",
#   "correct_answer": "True", "incorrect_answers": ["False"]},
#  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#   "question": "Romanian belongs to the Romance language family, shared with French, Spanish, Portuguese and Italian. ",
#   "correct_answer": "True", "incorrect_answers": ["False"]},
#  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#   "question": "Dihydrogen Monoxide was banned due to health risks after being discovered in 1983 inside swimming pools and drinking water.",
#   "correct_answer": "False", "incorrect_answers": ["True"]},
#  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#   "question": "Vietnam&#039;s national flag is a red star in front of a yellow background.", "correct_answer": "False",
#   "incorrect_answers": ["True"]}, {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                                    "question": "A pasodoble is a type of Italian pasta sauce.",
#                                    "correct_answer": "False", "incorrect_answers": ["True"]},
#  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#   "question": "Slovakia is a member of European Union-", "correct_answer": "True", "incorrect_answers": ["False"]},
#  {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#   "question": "The mitochondria is the powerhouse of the cell.", "correct_answer": "True",
#   "incorrect_answers": ["False"]}]


import requests
parameter = {"amount":10,"type":"boolean"}
response = requests.get(url="https://opentdb.com/api.php",params=parameter)
response.raise_for_status()
data = response.json()["results"]

