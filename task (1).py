#!/usr/bin/env python
# coding: utf-8

# In[16]:


import openai
import json

openai.api_key = ""


def generate_employee_auto_suggestions(partial_title, sector):
    prompt = f"Generate employee role suggestions in the {sector} sector for the partial title '{partial_title}'.\n\nSuggestions:"
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,
        max_tokens=50,
        stop=None)
    suggestions = response.choices[0].text.strip().split("\n")

    return suggestions

partial_title = "Specialist"
sector = "Health"
suggestions = generate_employee_auto_suggestions(partial_title, sector)

output_json = json.dumps({"sector": sector, "partial_title": partial_title, "suggestions": suggestions}, indent=4)
print(output_json)

        
partial_title = "Manager"
sector = "Technology"
suggestions = generate_employee_auto_suggestions(partial_title, sector)

output_json = json.dumps({"sector": sector, "partial_title": partial_title, "suggestions": suggestions}, indent=4)
print(output_json)

        
        
partial_title = "Professor"
sector = "Education"
suggestions = generate_employee_auto_suggestions(partial_title, sector)

output_json = json.dumps({"sector": sector, "partial_title": partial_title, "suggestions": suggestions}, indent=4)
print(output_json)


# In[18]:


def generate_employee_budget_auto_suggestion(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150, 
        stop=None  
    )
    return response.choices[0].text.strip()

def generate_hiring_plan(user_request):
    prompt = f"Generate a hiring plan for a {user_request['sector']} company.\n"
    prompt += f"The company is looking to allocate {user_request['budget_allocation']} of its budget on payroll for the next {user_request['years']} years.\n"
    prompt += "The available departments are: G&A, R&D, S&M, COGS.\n"
    prompt += f"The company prefers to focus on hiring roles that include {', '.join(user_request['focus_areas'])}.\n"
    prompt += "Please provide a list of potential employee roles, along with their departments, roles, yearly salaries, bonuses, and start dates.\n"

    generated_text = generate_employee_suggestions_budget(prompt)

    return generated_text

user_requests = [
    {
        "sector": "Technology",
        "budget_allocation": "70%",
        "years": 2,
        "focus_areas": ["Software Development", "Product Management"]
    },
    {
        "sector": "Healthcare",
        "budget_allocation": "60%",
        "years": 3,
        "focus_areas": ["Medical Research", "Patient Care"]
    }
]

output_data = []

for request in user_requests:
    hiring_plan_text = generate_hiring_plan(request)
    output_data.append({
        "user_request": request,
        "hiring_plan": hiring_plan_text
    })

print(json.dumps(output_data, indent=4))


# In[ ]:




