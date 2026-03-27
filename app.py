from flask import Flask, render_template, request, jsonify
import re
import urllib.request
from urllib.parse import urlparse

app = Flask(_name_)

# Fake news indicator keywords
FAKE_INDICATORS = [
    'shocking', 'unbelievable', 'you won\'t believe', 'miracle', 'secret',
    'they don\'t want you to know', 'exposed', 'cover up', 'conspiracy',
    'hoax', 'fake', 'fraud', 'scam', 'breaking', 'urgent', 'alert',
    'banned', 'censored', 'suppressed', 'hidden truth', 'wake up',
    'sheeple', 'mainstream media', 'deep state', 'illuminati', 'new world order',
    'must share', 'share before deleted', 'going viral', 'leaked'
]

CREDIBLE_INDICATORS = [
    'according to', 'research shows', 'study finds', 'experts say',
    'published in', 'peer reviewed', 'scientists', 'evidence suggests',
    'data shows', 'official statement', 'confirmed by', 'reported by',
    'sources say', 'investigation reveals', 'analysis shows'
]

CLICKBAIT_PATTERNS = [
    r'\b\d+ (reasons|ways|things|facts|secrets)\b',
    r'\bwhat happens next\b',
    r'\byou won\'t believe\b',
    r'\bthis is why\b',
    r'\beveryone is (talking|sharing)\b',
    r'!!+',
    r'\?\?+',
    r'\ball caps\b',
]

CREDIBLE_DOMAINS = [
    'bbc.com', 'reuters.com', 'apnews.com', 'theguardian.com',
    'nytimes.com', 'washingtonpost.com', 'npr.org', 'thehindu.com',
    'ndtv.com', 'timesofindia.com', 'indianexpress.com'
]

SUSPICIOUS_DOMAINS = [
    'infowars.com', 'naturalnews.com', 'beforeitsnews.com',
    'worldnewsdailyreport.com', 'empirenews.net'
]


def analyze_text(text):
    text_lower = text.lower()
    score = 50  # Start neutral
    reasons = []

    # Check fake indicators
    fake_count = sum(1 for word in FAKE_INDICATORS if word in text_lower)
    if fake_count > 0:
        score -= fake_count * 8
        reasons.append(f"Contains {fake_count} sensational/misleading keyword(s)")

    # Check credible indicators
    credible_count = sum(1 for word in CREDIBLE_INDICATORS if word in text_lower)
    if credible_count > 0:
        score += credible_count * 7
        reasons.append(f"Contains {credible_count} credibility indicator(s)")

    # Check clickbait patterns
    clickbait_count = sum(1 for p in CLICKBAIT_PATTERNS if re.search(p, text_lower))
    if clickbait_count > 0:
        score -= clickbait_count * 10
        reasons.append(f"Clickbait patterns detected")

    # Check excessive caps
    words = text.split()
    caps_words = sum(1 for w in words if w.isupper() and len(w) > 2)
    if caps_words > 3:
        score -= 10
        reasons.append("Excessive use of capital letters")

    # Check excessive punctuation
    if text.count('!') > 3 or text.count('?') > 3:
        score -= 8
        reasons.append("Excessive punctuation marks")

    # Check text length
    if len(text.split()) < 20:
        score -= 5
        reasons.append("Very short text - limited analysis possible")
    elif len(text.split()) > 100:
        score += 5
        reasons.append("Detailed article length")

    # Clamp score
    score = max(0, min(100, score))

    if score >= 65:
        verdict = "LIKELY REAL"
        color = "green"
    elif score >= 40:
        verdict = "UNCERTAIN"
        color = "orange"
    else:
        verdict = "LIKELY FAKE"
        color = "red"

    return {
        'verdict': verdict,
        'confidence': score,
        'color': color,
        'reasons': reasons if reasons else ["No strong indicators found"]
    }


def analyze_url(url):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower().replace('www.', '')

        if any(d in domain for d in CREDIBLE_DOMAINS):
            return {
                'verdict': 'CREDIBLE SOURCE',
                'confidence': 85,
                'color': 'green',
                'reasons': [f'{domain} is a recognized credible news source']
            }
        elif any(d in domain for d in SUSPICIOUS_DOMAINS):
            return {
                'verdict': 'SUSPICIOUS SOURCE',
                'confidence': 20,
                'color': 'red',
                'reasons': [f'{domain} is known for spreading misinformation']
            }
        else:
            return {
                'verdict': 'UNKNOWN SOURCE',
                'confidence': 50,
                'color': 'orange',
                'reasons': [f'{domain} is not in our verified sources database']
            }
    except:
        return {
            'verdict': 'INVALID URL',
            'confidence': 0,
            'color': 'red',
            'reasons': ['Could not parse the provided URL']
        }


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detect', methods=['POST'])
def detect():
    data = request.json
    text = data.get('text', '')
    url = data.get('url', '')

    if url:
        result = analyze_url(url)
    elif text:
        result = analyze_text(text)
    else:
        return jsonify({'error': 'No input provided'}), 400

    return jsonify(result)


if _name_ == '_main_':
    app.run(debug=True)