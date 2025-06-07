import doctly
import os

# Initialize the client with your API key
# export DOCTLY_API_KEY=sk-p1V37msR631ed6b478-7ez7kSmUM7RApN2fKoPKikAcSPCCczG2-Cdot46EjF1Kywhe9
api_key = os.getenv('DOCTLY_API_KEY')
client = doctly.Client(api_key=api_key)

# Convert a PDF file to Markdown
content = client.process('docs/Wolfspeed_C3M0016120K.pdf')
# Save the content to a Markdown file
with open('output.md', 'w') as markdown_file:
    markdown_file.write(content)