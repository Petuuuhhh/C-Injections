import re

sanitizedText = '[CIRCLE_1]Mueva el cursor a la letra que [MUS_DUMMY]quero con el[PLUS]Panel de control, luego [MUS_DUMMY]presiona el botón A para ingresar. [CIRCLE_2]Presione el botón B para retroceder. [CIRCLE_3]Presione SELECCIONAR para cambiar entre [MUS_DUMMY]letras mayúsculas y minúsculas. [CIRCLE_4]Presione el botón A en "Aceptar"'

# Identify and replace square brackets and their content with 'xxx'
matches = re.findall(r'\[.+?\]', sanitizedText)
for match in matches:
    sanitizedText = sanitizedText.replace(match, 'xxx', 1)

# Check if sanitizedText is less than 39 characters
if len(sanitizedText) <= 39:
    formatted_text = sanitizedText
else:
    # Split the string into sections of 39 characters without breaking words
    sections = re.findall(r'(.{1,39}\S(?:\s|$)|\S+)', sanitizedText)

    # Add '\\n' or '\\p' to the end of each section alternately
    formatted_sections = []
    for i, section in enumerate(sections):
        formatted_sections.append(section + ('\\p' if i % 2 else '\\n') if i < len(sections) - 1 else section)

    # Join the sections to form the final formatted string
    formatted_text = ''.join(formatted_sections)

# Replace 'xxx' with the original square brackets and their contents
for match in matches:
    formatted_text = formatted_text.replace('xxx', match, 1)

# Remove the space before '\\n' or '\\p'
formatted_text = formatted_text.replace(' \\n', '\\n').replace(' \\p', '\\p')

print(formatted_text)
