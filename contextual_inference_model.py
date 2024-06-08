"""
Author: Jacob Thomas Messer
Date: 2024-06-08
Description: This script leverages OpenAI’s GPT-4 API to generate detailed project plans based on 
randomly selected personas from a given JSON file. The script dynamically creates tailored prompts 
and fetches instructions from the GPT-4 model.
"""
import json
import random
import openai

# Load the personas from a JSON file
def load_personas(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)["personas"]

# Select a persona (randomly in this case)
def select_persona(personas):
    return random.choice(personas)

# Generate a prompt based on persona attributes
def generate_prompt(persona):
    name = persona["name"]
    role = persona["attributes"]["role"]
    skills = ", ".join(persona["attributes"]["skills"])
    experience = persona["attributes"]["experience"]
    
    prompt = f"""
    You are {name}, a {role} with skills in {skills} and {experience} of experience. 
    Based on your expertise, provide a detailed plan on how you would approach a new project involving these skills.
    """
    return prompt

# Send the prompt to GPT-4 and get the response
def get_gpt4_response(prompt):
    openai.api_key = 'your-openai-api-key'  # Replace with your actual OpenAI API key
    
    response = openai.Completion.create(
        model="text-davinci-004",
        prompt=prompt,
        max_tokens=500
    )
    
    return response.choices[0].text.strip()

# Main function
def main():
    json_file = 'personas.json'
    
    personas = load_personas(json_file)
    selected_persona = select_persona(personas)
    prompt = generate_prompt(selected_persona)
    
    instructions = get_gpt4_response(prompt)
    
    output_filename = f"instructions_for_{selected_persona['name'].lower()}.txt"
    with open(output_filename, 'w') as file:
        file.write(f"Instructions for {selected_persona['name']}:\n\n{instructions}")
    
    print(f"Instructions have been saved to {output_filename}")

if __name__ == "__main__":
    main()
