# Blog Automation with Claude AI

Flask API for optimizing blog content using Claude AI for SEO improvements, internal linking, and content freshness.

## Features

- SEO keyword identification and internal linking
- Automatic year updates for content freshness
- Natural CTA paragraph insertion
- REST API endpoint for n8n integration

## Quick Start

### 1. Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set your API key
export ANTHROPIC_API_KEY="your-api-key-here"

# Run the server
python blog_api.py
```

Server runs on `http://localhost:5000`

### 2. Deploy to Railway (Recommended)

1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) and sign up
3. Click "New Project" → "Deploy from GitHub repo"
4. Select this repository
5. Add environment variable:
   - Key: `ANTHROPIC_API_KEY`
   - Value: Your Anthropic API key
6. Railway will give you a public URL

### 3. Deploy to Render

1. Go to [render.com](https://render.com) and sign up
2. Click "New Web Service"
3. Connect your GitHub repo or upload files
4. Set environment variable `ANTHROPIC_API_KEY`
5. Deploy

## API Usage

### Endpoint: POST `/optimize-blog`

**Request:**
```json
{
  "blog_content": "Your blog content here..."
}
```

**Response:**
```json
{
  "success": true,
  "optimized_content": "SEO-optimized blog content...",
  "usage": {
    "input_tokens": 1234,
    "output_tokens": 5678
  }
}
```

**Test with curl:**
```bash
curl -X POST http://localhost:5000/optimize-blog \
  -H "Content-Type: application/json" \
  -d '{"blog_content": "Your test blog content..."}'
```

## n8n Integration

In your n8n workflow, add an **HTTP Request** node:

- **Method**: POST
- **URL**: `https://your-railway-app.railway.app/optimize-blog` (or your deployed URL)
- **Body Content Type**: JSON
- **Body**:
  ```json
  {
    "blog_content": "{{ $json.content }}"
  }
  ```

The optimized content will be in `$json.optimized_content`

## Files

- `blog_api.py` - Flask API server
- `blog.py` - Original standalone script
- `requirements.txt` - Python dependencies
- `Procfile` - Railway/Heroku deployment config
- `.env.example` - Environment variable template

## Environment Variables

- `ANTHROPIC_API_KEY` - Your Anthropic API key (required)

## Security

- Never commit `.env` files or API keys to git
- Use environment variables for all secrets
- The `.gitignore` file is configured to exclude sensitive files

## Support

For issues or questions about:
- Anthropic API: https://docs.anthropic.com/
- n8n: https://docs.n8n.io/
- Railway: https://docs.railway.app/
