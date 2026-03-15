import re


def check_password_strength(password):
    """
    Returns a dict with:
      - score: 0-4
      - label: 'Very Weak' | 'Weak' | 'Fair' | 'Strong' | 'Very Strong'
      - suggestions: list of improvement tips
    """
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Add at least one digit.")

    if re.search(r'[!@#$%^&*(),.?\":{}|<>_\-\[\]\/\\]', password):
        score += 1
    else:
        suggestions.append("Add at least one special character (!@#$%^&* etc.).")

    labels = {0: 'Very Weak', 1: 'Weak', 2: 'Fair', 3: 'Strong', 4: 'Strong', 5: 'Very Strong'}

    return {
        'score': score,
        'label': labels[score],
        'suggestions': suggestions
    }
