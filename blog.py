import anthropic

import os

client = anthropic.Anthropic(
    # Uses ANTHROPIC_API_KEY environment variable
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

# Replace placeholders like {{BLOG_CONTENT}} with real values,
# because the SDK does not support variables.
message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=20000,
    temperature=1,
    system="You are an SEO Content Optimization Assistant specialized in internal linking and content freshness updates.\n\nBelow is the blog content you need to process:\n{{BLOG_CONTENT}}\n\nYour task:\nAnalyze the above blog content and perform the following actions step-by-step.\n\n1. **Keyword Identification & Internal Linking**\n   - Identify the following SEO keywords or their closely related keywords and naturally insert internal links organically; at the same time, do not stuff the links:\n     • \"SAT mock test\" → https://galvanizetestprep.com/sat-prep/sat-practice-test/  \n     • \"SAT preparation\" or \"SAT prep\" → https://galvanizetestprep.com/sat-prep/  \n     • \"SAT app\" → https://galvanizetestprep.com/sat-prep/sat-app/  \n     • \"SAT score calculator\" → https://galvanizetestprep.com/sat-score-calculator/  \n     • \"bachelor's admission counselling\" → https://galvanizetestprep.com/undergraduation-admission-counselling/\n   - Use anchor text variations naturally if the exact keyword is missing (e.g., \"start your SAT prep journey\" → link to SAT Preparation).\n   - Follow SEO internal linking best practices:\n     - Place links contextually within sentences (not in headers).\n     - Avoid keyword stuffing and repetitive linking.\n     - One link per keyword per blog.\n     - Keep existing links intact and active.\n     - Format all links as standard HTML `<a>` tags with:\n       `target=\"_blank\"` and `rel=\"noopener\"`.\n       Example: `<a href=\"https://galvanizetestprep.com/sat-prep/\" target=\"_blank\" rel=\"noopener\">SAT preparation</a>`\n\n2. **Backlink Creation (if none exist)**\n   - If no relevant internal links are present in the content, add a related keyword in the content naturally and create an internal link, and add a natural CTA paragraph at the end or near the conclusion.\n   - Example:\n     `<p>Looking to ace your SAT? Start your <a href=\"https://galvanizetestprep.com/sat-prep/\" target=\"_blank\" rel=\"noopener\">SAT preparation</a> today with free <a href=\"https://galvanizetestprep.com/sat-prep/sat-practice-test/\" target=\"_blank\" rel=\"noopener\">SAT mock tests</a> from Galvanize.</p>`\n\n3. **Update Year & Freshness**\n   - Replace outdated year mentions (2020, 2021, 2022, 2023, 2024) with **2025**.\n   - If a phrase like “SAT 2021 format” appears, update it contextually to “latest SAT 2025 format”.\n   - Ensure all statements reflect relevance to the end of 2025.\n\n4. **Content & Format Preservation**\n   - Maintain original formatting (HTML/Markdown), structure, tone, and readability.\n   - Do not add explanations or comments.\n   - Output only the **optimized blog content** (not JSON or additional metadata).\n\nFinal output should contain only the updated, SEO-optimized blog content.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "You are an SEO Content Optimization Assistant specialized in internal linking and content freshness updates.\n\nBelow is the blog content you need to process:\n{{BLOG_CONTENT}}\n\nYour task:\nAnalyze the above blog content and perform the following actions step-by-step.\n\n1. **Keyword Identification & Internal Linking**\n   - Identify the following SEO keywords or their closely related keywords and naturally insert internal links organically; at the same time, do not stuff the links:\n     • \"SAT mock test\" → https://galvanizetestprep.com/sat-prep/sat-practice-test/  \n     • \"SAT preparation\" or \"SAT prep\" → https://galvanizetestprep.com/sat-prep/  \n     • \"SAT app\" → https://galvanizetestprep.com/sat-prep/sat-app/  \n     • \"SAT score calculator\" → https://galvanizetestprep.com/sat-score-calculator/  \n     • \"bachelor's admission counselling\" → https://galvanizetestprep.com/undergraduation-admission-counselling/\n   - Use anchor text variations naturally if the exact keyword is missing (e.g., \"start your SAT prep journey\" → link to SAT Preparation).\n   - Follow SEO internal linking best practices:\n     - Place links contextually within sentences (not in headers).\n     - Avoid keyword stuffing and repetitive linking.\n     - One link per keyword per blog.\n     - Keep existing links intact and active.\n     - Format all links as standard HTML `<a>` tags with:\n       `target=\"_blank\"` and `rel=\"noopener\"`.\n       Example: `<a href=\"https://galvanizetestprep.com/sat-prep/\" target=\"_blank\" rel=\"noopener\">SAT preparation</a>`\n\n2. **Backlink Creation (if none exist)**\n   - If no relevant internal links are present in the content, add a related keyword in the content naturally and create an internal link, and add a natural CTA paragraph at the end or near the conclusion.\n   - Example:\n     `<p>Looking to ace your SAT? Start your <a href=\"https://galvanizetestprep.com/sat-prep/\" target=\"_blank\" rel=\"noopener\">SAT preparation</a> today with free <a href=\"https://galvanizetestprep.com/sat-prep/sat-practice-test/\" target=\"_blank\" rel=\"noopener\">SAT mock tests</a> from Galvanize.</p>`\n\n3. **Update Year & Freshness**\n   - Replace outdated year mentions (2020, 2021, 2022, 2023, 2024) with **2025**.\n   - If a phrase like “SAT 2021 format” appears, update it contextually to “latest SAT 2025 format”.\n   - Ensure all statements reflect relevance to the end of 2025.\n\n4. **Content & Format Preservation**\n   - Maintain original formatting (HTML/Markdown), structure, tone, and readability.\n   - Do not add explanations or comments.\n   - Output only the **optimized blog content** (not JSON or additional metadata).\n\nFinal output should contain only the updated, SEO-optimized blog content."
                }
            ]
        }
    ],
    thinking={
        "type": "enabled",
        "budget_tokens": 16000
    }
)
print(message.content)