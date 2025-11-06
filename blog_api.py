from flask import Flask, request, jsonify
import anthropic
import os

app = Flask(__name__)

# Initialize Anthropic client
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

SYSTEM_PROMPT = """You are an SEO Content Optimization Assistant specialized in internal linking and content freshness updates.

Below is the blog content you need to process:
{{BLOG_CONTENT}}

Your task:
Analyze the above blog content and perform the following actions step-by-step.

1. **Keyword Identification & Internal Linking**
   - Identify the following SEO keywords or their closely related keywords and naturally insert internal links organically; at the same time, do not stuff the links:
     • "SAT mock test" → https://galvanizetestprep.com/sat-prep/sat-practice-test/
     • "SAT preparation" or "SAT prep" → https://galvanizetestprep.com/sat-prep/
     • "SAT app" → https://galvanizetestprep.com/sat-prep/sat-app/
     • "SAT score calculator" → https://galvanizetestprep.com/sat-score-calculator/
     • "bachelor's admission counselling" → https://galvanizetestprep.com/undergraduation-admission-counselling/
   - Use anchor text variations naturally if the exact keyword is missing (e.g., "start your SAT prep journey" → link to SAT Preparation).
   - Follow SEO internal linking best practices:
     - Place links contextually within sentences (not in headers).
     - Avoid keyword stuffing and repetitive linking.
     - One link per keyword per blog.
     - Keep existing links intact and active.
     - Format all links as standard HTML `<a>` tags with:
       `target="_blank"` and `rel="noopener"`.
       Example: `<a href="https://galvanizetestprep.com/sat-prep/" target="_blank" rel="noopener">SAT preparation</a>`

2. **Backlink Creation (if none exist)**
   - If no relevant internal links are present in the content, add a related keyword in the content naturally and create an internal link, and add a natural CTA paragraph at the end or near the conclusion.
   - Example:
     `<p>Looking to ace your SAT? Start your <a href="https://galvanizetestprep.com/sat-prep/" target="_blank" rel="noopener">SAT preparation</a> today with free <a href="https://galvanizetestprep.com/sat-prep/sat-practice-test/" target="_blank" rel="noopener">SAT mock tests</a> from Galvanize.</p>`

3. **Update Year & Freshness**
   - Replace outdated year mentions (2020, 2021, 2022, 2023, 2024) with **2025**.
   - If a phrase like "SAT 2021 format" appears, update it contextually to "latest SAT 2025 format".
   - Ensure all statements reflect relevance to the end of 2025.

4. **Content & Format Preservation**
   - Maintain original formatting (HTML/Markdown), structure, tone, and readability.
   - Do not add explanations or comments.
   - Output only the **optimized blog content** (not JSON or additional metadata).

Final output should contain only the updated, SEO-optimized blog content."""

@app.route('/optimize-blog', methods=['POST'])
def optimize_blog():
    try:
        # Get blog content from request
        data = request.get_json()

        if not data or 'blog_content' not in data:
            return jsonify({
                'error': 'Missing blog_content in request body'
            }), 400

        blog_content = data['blog_content']

        # Replace placeholder in system prompt
        system_prompt = SYSTEM_PROMPT.replace('{{BLOG_CONTENT}}', blog_content)
        user_prompt = SYSTEM_PROMPT.replace('{{BLOG_CONTENT}}', blog_content)

        # Call Claude API
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=20000,
            temperature=1,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user_prompt
                        }
                    ]
                }
            ],
            thinking={
                "type": "enabled",
                "budget_tokens": 16000
            }
        )

        # Extract optimized content from response
        optimized_content = ""
        for block in message.content:
            if block.type == "text":
                optimized_content += block.text

        return jsonify({
            'success': True,
            'optimized_content': optimized_content,
            'usage': {
                'input_tokens': message.usage.input_tokens,
                'output_tokens': message.usage.output_tokens
            }
        }), 200

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
